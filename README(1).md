
# Sensor Data Streaming Using Kafka and HDFS

This project demonstrates a real-time sensor data pipeline using **Apache Kafka** and **Hadoop Distributed File System (HDFS)**. It was developed as part of the DSA 5620 – Big Data Analytics course at the University of Central Missouri.

## 👩‍💻 Developed by
**Zahra Dastfal**  
Graduate Student – Data Science & Artificial Intelligence  
[LinkedIn Profile](https://www.linkedin.com/in/zahradastfal)

---

## 📌 Project Overview

- **Simulate real-time sensor data** (e.g., temperature, humidity)
- **Stream data via Apache Kafka** using a Python Kafka producer
- **Receive and save data** with a Python Kafka consumer
- **Transfer data to Ubuntu VM** using a shared folder
- **Upload the JSON file into HDFS** for distributed storage

---

## ⚙️ Tools & Technologies

- `Apache Kafka` for streaming messages
- `Kafka-Python` library for producer and consumer
- `HDFS` (Hadoop) for data storage
- `Oracle VirtualBox` with `Ubuntu` as the VM
- `Python 3` for scripting
- Shared Folders between Windows host and Ubuntu guest

---

## 🧱 Kafka Architecture Used

- **Producer:** Python script generating fake sensor data every 2 seconds
- **Topic:** `sensor-data` (Kafka topic for messages)
- **Consumer:** Python script saving incoming messages into a JSON file
- **Zookeeper & Kafka Server:** Managed from Windows terminal
- **HDFS:** JSON file uploaded to custom directory `/user/zahra/sensor_datatype/`

---

## 📂 File Structure

```
project/
├── sensor_producer.py         # Kafka producer sending sensor data
├── sensor_consumer.py         # Kafka consumer saving data to JSON
├── sensor_data_sample.json    # Output JSON file with sensor readings
└── README.md                  # Project documentation
```

---

## 🖼️ Screenshots

- ✅ Kafka Producer Running
- ✅ Kafka Consumer Receiving Data
- ✅ JSON File Transferred to Ubuntu
- ✅ File Uploaded and Visible in HDFS

(See presentation slides for visuals.)

---

## 🚀 How to Run the Project

1. **Start Zookeeper**
   ```
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```

2. **Start Kafka**
   ```
   bin/kafka-server-start.sh config/server.properties
   ```

3. **Create Kafka Topic**
   ```
   bin/kafka-topics.sh --create --topic sensor-data --bootstrap-server localhost:9092
   ```

4. **Run Producer**
   ```
   python sensor_producer.py
   ```

5. **Run Consumer (separate terminal)**
   ```
   python sensor_consumer.py
   ```

6. **Move the JSON file to shared folder and upload to HDFS**
   ```
   hdfs dfs -put /media/sf_project/sensor_data_sample.json /user/zahra/sensor_datatype/
   ```

---

## 📘 What I Learned

- End-to-end Kafka pipeline setup
- Using Python for data generation and ingestion
- Working with shared folders in VirtualBox
- Uploading data to HDFS using CLI
- Integrating streaming tools with big data frameworks

---

## 📣 License

This project is for academic and educational purposes. Feel free to explore, learn, and improve it!
