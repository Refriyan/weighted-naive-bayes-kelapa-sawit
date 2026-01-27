import os
import logging
import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['UPLOAD_FOLDER'] = os.path.join('web_app', 'static', 'uploads')
app.config['TRAINING_FOLDER'] = os.path.join('web_app', 'oil_palm')

# Create the uploads folder if it does not exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['TRAINING_FOLDER']):
    os.makedirs(app.config['TRAINING_FOLDER'])

# Allowed extensions for file uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_color_histogram(image, bins=(8, 8, 8)):
    hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

# Load and prepare the dataset
def prepare_dataset():
    data_dir = app.config['TRAINING_FOLDER']
    X = []
    y = []

    for label, folder_name in enumerate(["matang", "terlalu_matang", "tidak_matang"]):
        folder_path = os.path.join(data_dir, folder_name)
        for file_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, file_name)
            try:
                image = cv2.imread(image_path)
                if image is not None:
                    image = cv2.resize(image, (256, 256))
                    color_hist_features = extract_color_histogram(image)
                    X.append(color_hist_features)
                    y.append(label)
            except Exception as e:
                logging.warning(f"Failed to process image {image_path}: {e}")

    X = np.array(X)
    y = np.array(y)
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
def train_models():
    X_train, X_test, y_train, y_test = prepare_dataset()
    
    # Calculate class weights
    class_counts = np.bincount(y_train)
    class_weights = {i: sum(class_counts) / count for i, count in enumerate(class_counts)}

    model_wnb = GaussianNB(priors=None, var_smoothing=1e-09)
    model_wnb.fit(X_train, y_train, sample_weight=[class_weights[label] for label in y_train])
    wnb_accuracy = accuracy_score(y_test, model_wnb.predict(X_test))

    model_nb = MultinomialNB()
    model_nb.fit(X_train, y_train)
    nb_accuracy = accuracy_score(y_test, model_nb.predict(X_test))

    return model_wnb, model_nb, int(wnb_accuracy * 100), int(nb_accuracy * 100)  # Convert to integer percentage

model_wnb, model_nb, wnb_accuracy, nb_accuracy = train_models()

# Dummy palm fruit detection model (replace with a proper model)
def is_palm_fruit(image):
    # Simple heuristic: check if the average color is within a certain range
    avg_color = cv2.mean(image)[:3]
    return 50 < avg_color[0] < 200 and 30 < avg_color[1] < 180 and 20 < avg_color[2] < 170

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

    try:
        image = cv2.imread(file_path)
        if image is not None:
            image = cv2.resize(image, (256, 256))
            color_hist_features = extract_color_histogram(image)
            X = [color_hist_features]
            X = np.array(X)

            selected_model = request.form.get('model')
            if selected_model == 'wnb':
                prediction = model_wnb.predict(X)
                accuracy = wnb_accuracy  # Use integer accuracy
            else:
                prediction = model_nb.predict(X)
                accuracy = nb_accuracy  # Use integer accuracy

            label_mapping = {0: "ripe", 1: "overripe", 2: "unripe"}
            result = label_mapping[prediction[0]]

            # Generate histogram image for display
            plt.ioff()  # Turn off interactive mode
            plt.figure(figsize=(8, 6))
            plt.bar(range(len(color_hist_features)), color_hist_features)
            plt.xlabel('Bins')
            plt.ylabel('Frequency')
            plt.title('Color Histogram')
            histogram_filename = 'histogram.png'
            histogram_path = os.path.join(app.config['UPLOAD_FOLDER'], histogram_filename)
            plt.savefig(histogram_path)
            plt.close()

            return render_template('result.html', result=result, accuracy=accuracy, file_path=filename, histogram_path=histogram_filename)
    except Exception as e:
        logging.warning(f"Failed to process uploaded file {file_path}: {e}")
        flash('Failed to process uploaded image.')
        return redirect(request.url)

    flash('Invalid file type')
    return redirect(url_for('index'))

@app.route('/retrain', methods=['POST'])
def retrain():
    global model_wnb, model_nb, wnb_accuracy, nb_accuracy
    model_wnb, model_nb, wnb_accuracy, nb_accuracy = train_models()
    flash('Models retrained successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
