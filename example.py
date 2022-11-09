from ocr import NNRecognizer
from pathlib import Path

nnRecognizer = NNRecognizer(model_file="nn_model.onnx")
result = nnRecognizer.recognize(Path('captcha.jpg').read_bytes())
print(result)
