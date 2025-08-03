# 🚨 Real-Time Fraud Detection with PySpark, Kafka, and MLlib

A real-time fraud detection pipeline that ingests transaction data via Kafka, processes it with PySpark Structured Streaming, and classifies transactions using a machine learning model built with Spark MLlib.

---

## 📌 Features

- 🔄 Real-time data ingestion using Apache Kafka  
- ⚙️ Stream processing with PySpark Structured Streaming  
- 🤖 Logistic Regression-based fraud prediction using Spark MLlib  
- 🗃️ Offline model training pipeline  
- 📦 Dockerized Kafka (Zookeeper + Kafka Broker)

---

## 🧰 Tech Stack

- Python 3  
- Apache Spark (PySpark)  
- Apache Kafka  
- Spark MLlib  
- Docker  
- WSL (Windows Subsystem for Linux) for compatibility

---

## 🧠 Model Overview

- **Model Type**: Logistic Regression  
- **Training Data**: Synthetic transaction dataset  
- **Features Used**: Transaction amount, transaction type, etc.  
- **Label**: Binary fraud classification (0 = legit, 1 = fraud)

---

## 🗂️ Project Structure

```
fraud_project/
├── data/                      # Training data (CSV)
├── spark_job/
│   ├── spark_stream.py        # Real-time stream processor
│   ├── producer.py            # Kafka producer (pushes transactions)
│   └── __init__.py
├── train_model.py             # Offline model training script
├── fraud_model/               # Saved MLlib model (Spark pipeline)
├── docker-compose.yml         # Kafka + Zookeeper stack
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fraud_project.git
cd fraud_project
```

### 2. Start Kafka Services

```bash
docker-compose up -d
```

### 3. Train the Model

```bash
python3 train_model.py
```

### 4. Start the Kafka Producer

```bash
python3 spark_job/producer.py
```

### 5. Run the Streaming Job

```bash
python3 spark_job/spark_stream.py
```

---

## 🧪 Sample Output

- Incoming transaction printed to console
- Model prediction: `FRAUD` or `LEGIT`

---

## 🛠️ Troubleshooting

- **Permission errors on Windows?** Use WSL (recommended)
- **Spark Streaming can't find Kafka source?** Ensure you have the Kafka Spark package in `PYSPARK_SUBMIT_ARGS`

---

## 📈 Future Enhancements

- Model accuracy optimization with advanced features  
- Integration with alert systems (Slack, email)  
- Dashboard for monitoring stream output  

---

## 🤝 Contributing

Pull requests welcome. For major changes, please open an issue first.

---

## 📄 License

MIT License
