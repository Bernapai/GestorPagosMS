# GestorPagos 💳📊  

**GestorPagos** es un proyecto backend basado en una arquitectura de microservicios para la gestión de pagos y reportes financieros. Implementa **Django** para la creación de APIs REST, **MySQL** como base de datos, **RabbitMQ** para la comunicación entre microservicios y **Docker** para la contenerización. Además, utiliza **Kong** como **API Gateway** para la autenticación, autorización y redirección de solicitudes.

---

## 🌍 Arquitectura del Sistema  
El sistema está compuesto por varios microservicios independientes que permiten una gestión eficiente de pagos y operaciones financieras:  

### **API Gateway (Kong) 🌐**
- Redirige las solicitudes a los microservicios correspondientes.  
- Maneja la autenticación y autorización mediante **tokens JWT**.

---

## 🖥️ Microservicios  

### **Servicio de Gestión de Usuarios (Users) 👥**  
- **Endpoint:** `/users`  
- **Funcionalidad:** Registro, autenticación y administración de usuarios.  

### **Servicio de Transacciones (Transactions) 💸**  
- **Endpoint:** `/transactions`  
- **Funcionalidad:** Registro, consulta y validación de transacciones financieras.  

### **Servicio de Reportes (Reports) 📊**  
- **Endpoint:** `/reports`  
- **Funcionalidad:** Generación de reportes detallados sobre pagos y transacciones.  

### **Servicio de Notificaciones (Notifications) 📩**  
- **Endpoint:** `/notifications`  
- **Funcionalidad:** Envío de alertas y notificaciones relacionadas con pagos.  

---

## 🔧 Tecnologías Utilizadas  

- **Django:** Framework robusto para el desarrollo backend.  
- **MySQL/MongoDB:** Base de datos relacional Y no relacional para almacenar datos de usuarios, transacciones y reportes.  
- **Docker:** Contenerización de cada microservicio para facilitar el despliegue.  
- **JWT (JSON Web Tokens):** Autenticación y autorización de usuarios.  
- **Kong:** API Gateway para la administración centralizada de solicitudes.  
- **RabbitMQ:** Comunicación eficiente entre los microservicios.  
