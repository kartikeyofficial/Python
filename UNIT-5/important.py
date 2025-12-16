import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Define roadmap sections and their contents
roadmap = {
    "Foundations": [
        "Java Core (OOP, Collections, Streams)",
        "Git, GitHub",
        "IntelliJ, Eclipse",
        "Maven, Gradle",
        "JUnit, Mockito"
    ],
    "Frontend": [
        "HTML, CSS, JavaScript",
        "React / Angular / Vue",
        "Bootstrap / Tailwind",
        "Redux / NgRx",
        "Jest, Cypress"
    ],
    "Backend (Java)": [
        "Spring Boot, Spring MVC",
        "Spring Security, JWT",
        "REST APIs, Swagger",
        "Spring Cloud, Eureka",
        "Kafka, RabbitMQ"
    ],
    "Database": [
        "MySQL, PostgreSQL",
        "Hibernate, JPA",
        "MongoDB, Redis",
        "Flyway, Liquibase"
    ],
    "DevOps & Deployment": [
        "Docker, Kubernetes",
        "Jenkins, GitHub Actions",
        "AWS / GCP / Azure",
        "Prometheus, Grafana"
    ],
    "Soft Skills & Practices": [
        "SOLID, DRY, KISS",
        "Design Patterns",
        "Markdown, JavaDoc",
        "Agile, Scrum"
    ],
    "Advanced Topics": [
        "WebSockets, GraphQL",
        "Reactive (WebFlux)",
        "Serverless (AWS Lambda)",
        "Concurrency, DDD"
    ]
}

# Setup the plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

# Colors for each category
colors = [
    "#ff9999", "#66b3ff", "#99ff99", "#ffcc99",
    "#c2c2f0", "#ffb3e6", "#b3d9ff"
]

# Draw each section as a box
y = 1.0
for i, (section, items) in enumerate(roadmap.items()):
    color = colors[i % len(colors)]
    text = f"{section}\n" + "\n".join(f" - {item}" for item in items)
    ax.text(0.5, y, text, ha='center', va='top', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.5", facecolor=color, edgecolor='black'))
    y -= 0.14 + 0.02 * len(items)

plt.tight_layout()
plt.show()
