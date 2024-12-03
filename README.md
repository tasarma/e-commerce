
# 🚧 UNDER DEVELOPMENT 🚧

## E-WAREHOUSE

### Table of Contents
1. [Overview](#overview)
2. [Technologies](#technologies)
3. [Technical Details](#technical-details)
4. [Installation](#installation)
5. [Getting Started](#getting-started)
6. [Usage](#usage)
7. [Demo](#demo)
8. [Contributing](#contributing)
9. [Roadmap](#roadmap)
10. [Security Notice](#security-notice)
11. [License](#license)

---

## Overview

👉 **Empowers pharmaceutical warehouses** to market their products directly to pharmacies.  
👉 **Facilitates medicine exchange** between pharmacies, a legal activity regulated by the Republic of Türkiye Ministry of Health.  
👉 **Expands with new features** to support a wide range of pharmacy needs.

---

### Technologies

| Technology    | Version |
|---------------|---------|
| [![Django][Django]][Django-url] | 5.0.4 |
| [![React][React.js]][React-url] | 18.3.1 |
| [![PostgreSQL][PostgreSql]][PostgreSql-url] | 14.5 |

| Tools |
|-------|
| [![Bootstrap][Bootstrap]][Bootstrap-url] |
| [![Redux][Redux]][Redux-url] |
| [![Poetry][Poetry]][Poetry-url] |
| ![PyTest][PyTest] |
| [![Anaconda][Anaconda]][Anaconda-url] |

---

### Technical Details

#### 🏛️ Multitenant Architecture

To support multiple organizations, we employ a **row-based data segregation strategy** for efficient resource usage and easy scalability.

**Why Row-Based Segregation?**  
- **Cost Efficiency:** Multiple tenants share the same database instance, reducing infrastructure costs.  
- **Lower Maintenance:** A single database instance simplifies management.  
- **Dynamic Tenancy:** Easily add new tenants without additional setup.  
- **Customization:** Supports tenant-specific features within a shared environment.

**Note:** While high load by one tenant could impact others, our anticipated transaction volume makes this a feasible approach.

---

## 🛠 Installation

### Prerequisites

1. **Install Anaconda or Install PyEnv**  
2. **Create Environment**  
   ```sh
   conda create --name ewarehouse python=3.12
   ```
3. **Install Chocolatey (Windows only)**  
4. **Install Make with Chocolatey**  
   ```sh
   choco install make
   ```
5. **Install Poetry**  
   Change directory to **backend**
   ```sh
   pip install poetry
   ```
6. **Install Dependencies**  
    Delete **poetry.lock** file
   ```sh
   make install 
   ```
7. **Clone the repository**  
   ```sh
   git clone https://github.com/tasarma/
   ```
8. **Edit `hosts` file**  
   **Windows**  
   `C:\Windows\System32\drivers\etc\hosts`:  
   ```plaintext
   127.0.0.1 kubernetes.docker.internal
   127.0.0.1 tenantone.example.com
   127.0.0.1 tenanttwo.example.com
   ```
   **Linux**  
   `/etc/hosts`:  
   ```plaintext
   127.0.0.1 kubernetes.docker.internal
   127.0.0.1	localhost tenantone.example.com 
   127.0.0.1	localhost tenanttwo.example.com

   ```
9. **Run Migrations**  
   ```sh
   make migrate
   make run
   ```

10. **Install Frontend Packages**  
   Change directory to **frontend**
   
   Delete **package-lock.json** file
   ```sh
   npm install
   make run
   ```
11. **Install Redux DevTools** on Chrome.
12. **On Successful Backend Installation**  
   **Visit:**  http://tenantone.example.com:8000/api/docs/
   
   ![API Schema](/public/ApiSchema.png)

12. **On Successful Frontend Installation**  
   **Visit:**  http://tenantone.example.com:3000
   
   ![Front End](/public/frontend.png)
---

## 🚀 Getting Started

Follow these steps to run the application locally:

1. **Open the project in VS Code**  
2. **Run backend and frontend** (in separate terminals):  
   ```sh
   cd backend
   make run
   ```
   ```sh
   cd frontend
   make run
   ```

---

## Demo

![E-Warehouse Demo](/public/demo.gif)

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

Please ensure your PR description clearly describes the changes and their benefits.

---

## Roadmap

- ✅ User authentication
- [ ] Payment integration
- [ ] PostgreSQL integration
- [ ] Docker integration

---

## Security Notice

Ensure compliance with all legal and data protection regulations when handling pharmaceutical data.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](/public/LICENSE) file for details.

---

<!-- MARKDOWN LINKS & IMAGES -->
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/
[PostgreSql]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSql-url]: https://www.postgresql.org/
[Bootstrap]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/
[Redux]: https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white
[Redux-url]: https://redux.js.org/
[Poetry]: https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D
[Poetry-url]: https://python-poetry.org/
[PyTest]: https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3
[Anaconda]: https://img.shields.io/badge/Anaconda-44A833?style=for-the-badge&logo=anaconda&logoColor=white
[Anaconda-url]: https://www.anaconda.com/
