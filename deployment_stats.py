import time
import torch
from ultralytics import YOLO

def profile_deployment(model_path, source_video):
    # Load model to GPU if available
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = YOLO(model_path).to(device)
    
    print(f"--- Deployment Profiling on {device.upper()} ---")
    
    # Warm-up run (common in research to stabilize hardware)
    model.predict(source=source_video, imgsz=640, conf=0.25, save=False, stream=True, max_det=1)

    start_time = time.time()
    results = model.predict(source=source_video, imgsz=640, conf=0.25, save=False, stream=True)
    
    frame_counts = 0
    latencies = []

    for r in results:
        # Calculate latency for each frame
        frame_lat = r.speed['inference']  # Latency in milliseconds
        latencies.append(frame_lat)
        frame_counts += 1

    total_time = time.time() - start_time
    avg_latency = sum(latencies) / len(latencies)
    fps = frame_counts / total_time

    print(f"\n--- Analysis Results ---")
    print(f"Total Frames Processed: {frame_counts}")
    print(f"Average Inference Latency: {avg_latency:.2f} ms")
    print(f"Estimated Throughput (FPS): {fps:.2f}")
    print(f"Optimization Status: {'Ready for Edge Deployment' if avg_latency < 30 else 'Requires Quantization'}")

if __name__ == "__main__":
    # Update these paths based on your repo structure
    profile_deployment('yolov8n.pt', 'path/to/your/test_video.mp4')