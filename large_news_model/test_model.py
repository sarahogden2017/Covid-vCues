from numpy import loadtxt
from tensorflow.keras.models import load_model

# load model
model = load_model('best_model.keras')

# summarize model
model.summary()
