# MachineVision-WrapperAnomaly
- "Wrapper Anomaly Detection" is the main logic for the anomaly detections in wrappers
- The logic is mainly built for Medicine Wrapper to detects the anomaly in printing of Batch Number, Expiry Dates, etc.
- The code register the images as a part of preprocessing to overcome the issue of image orientation
- It compares reference image with every other images to find anomaly in printing
