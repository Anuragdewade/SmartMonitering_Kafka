# AI-Powered Real-Time Smart Monitoring System

A real-time distributed monitoring system built using **Python, Apache Kafka, FastAPI, Docker, and AI-based alert logic**.

This project demonstrates:
- Real-time data streaming
- Distributed systems architecture
- Producer-consumer communication
- Dockerized Kafka deployment
- AI-based alert generation
- Event-driven backend engineering

---

# Project Overview

The system continuously generates sensor temperature data and streams it through Apache Kafka. A Kafka consumer receives the data and sends it to an AI analysis service built using FastAPI.

If the temperature exceeds a threshold value, the AI service generates an alert.

This project simulates an industrial smart monitoring system used in:
- Smart factories
- IoT systems
- Healthcare monitoring
- Industrial automation
- Real-time analytics systems

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API framework |
| Apache Kafka | Real-time event streaming |
| Docker | Containerization |
| Zookeeper | Kafka coordination |
| kafka-python | Kafka integration |
| Requests | API communication |

---

# System Architecture

```plaintext
Temperature Sensor Simulator
            ↓
      Kafka Producer
            ↓
       Kafka Topic
            ↓
      Kafka Consumer
            ↓
        AI Service
            ↓
 Dashboard / Backend API
