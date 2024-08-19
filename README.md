

# Financial Fraud Detection Using Deep Learning


https://github.com/user-attachments/assets/ae62bd50-42ef-4814-8423-5160b90e4082


## Project Overview

This project focuses on detecting financial fraud using deep learning techniques. The model leverages various deep learning architectures to identify fraudulent transactions in a financial dataset. The primary goals are to build, train, and evaluate a deep learning model to detect anomalies and fraudulent activities effectively.

## Repository Structure

- `app.py`: Streamlit application for making predictions using the trained deep learning model.
- `model.h5`: Trained deep learning model saved in HDF5 format.
- `requirements.txt`: List of Python dependencies required to run the project.
- `data/`: Directory containing dataset files.
- `notebooks/`: Jupyter notebooks for data exploration and model training (if applicable).

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- TensorFlow
- Streamlit
- Other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shubh123a3/Financial-Fraud-Detection-Using-Deep-Learning.git
   cd Financial-Fraud-Detection-Using-Deep-Learning
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Streamlit App

1. Ensure the model file `model.h5` is in the root directory of the project.

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open the provided URL in your browser to interact with the application.

### Using the Model

1. The app allows you to input various features related to financial transactions.
2. Click the "Predict" button to get the model's prediction on whether the transaction is fraudulent.

## Model Training

For training the model, refer to the Jupyter notebooks in the `notebooks/` directory. The model training involves:

- Data preprocessing
- Model architecture definition
- Training the model
- Saving the model as `model.h5`

## Troubleshooting

- **FileNotFoundError**: Ensure the `model.h5` file is located in the same directory as `app.py`. Check the path and file existence.
- **ModuleNotFoundError**: Install missing modules using `pip install <module>`.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Please ensure that your contributions align with the project's objectives.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- TensorFlow for deep learning framework
- Streamlit for building the web application
- Dataset providers and any other contributors


