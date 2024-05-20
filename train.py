from ultralytics import YOLO

 #Load a model
#  # build a new model from YAML
model = YOLO(r'C:\pd_anomaly_detection\PD___Anomaly_Detection\runs\detect\train3\weights\last.pt')  # load a pretrained model (recommended for training)
#  # build from YAML and transfer weights

# # Train the model
results = model.train(data=r"C:\pd_anomaly_detection\PD___Anomaly_Detection\conedataset10000images\data.yaml", epochs=120, imgsz=640,save=True,save_period=1,device='cpu')
