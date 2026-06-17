import onnxruntime as ort
import numpy as np

# Local ONNX model — NOT a HuggingFace model
# Covers: AIBOM-30 (non-HuggingFace model edge case)
# Expected: model listed in AIBOM viewer BUT "View AIBOM" download shows error for this component
# since aetheris-ai/aibom-generator only supports HuggingFace models

LOCAL_MODEL_PATH = "./models/classifier.onnx"


def run_inference(input_data: np.ndarray) -> np.ndarray:
    session = ort.InferenceSession(LOCAL_MODEL_PATH)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    result = session.run([output_name], {input_name: input_data})
    return result[0]
