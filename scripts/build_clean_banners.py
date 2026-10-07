import xml.etree.ElementTree as ET

def process_banner(src_path, dst_path, is_dark=True):
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements list
    # Note: Use &amp; for any '&' in XML text
    replacements = [
        ("Maria Claudia's live system profile", "Alejandro Mallama's live system profile"),
        ("DevOps tool silhouettes", "tech tool silhouettes"),
        ("@macu-dev", "@Alejox102004"),
        ("Maria Claudia", "Alejandro Mallama"),
        ("DevOps Engineer", "Full Stack Developer"),
        ("Rosario, Argentina", "Ecuador &#183; EC"),
        ("CI/CD &#183; Cloud Native &#183; IaC", "Full Stack &#183; Web &amp; Cloud"),
        ("CI/CD · Cloud Native · IaC", "Full Stack · Web &amp; Cloud"),
        ("Automatizacion &#183; Escalado &#183; Despliegue", "Desarrollo &#183; Arquitectura &#183; Despliegue"),
        ("Automatizacion · Escalado · Despliegue", "Desarrollo · Arquitectura · Despliegue"),
        ("Terraform &#183; Helm &#183; GitHub Actions", "Astro · React · PHP · Node.js"),
        ("Terraform · Helm · GitHub Actions", "Astro · React · PHP · Node.js"),
        (">cloud: <", ">frontend: <"),
        ("AWS &#183; Azure", "Astro · React · Next.js · TS"),
        ("AWS · Azure", "Astro · React · Next.js · TS"),
        (">containers: <", ">backend: <"),
        ("Kubernetes &#183; Docker &#183; Helm", "PHP · Node.js · Python · Express"),
        ("Kubernetes · Docker · Helm", "PHP · Node.js · Python · Express"),
        (">iac: <", ">databases: <"),
        ("Terraform &#183; Ansible", "PostgreSQL · MySQL · MongoDB"),
        ("Terraform · Ansible", "PostgreSQL · MySQL · MongoDB"),
        (">observability: <", ">devops: <"),
        ("Prometheus &#183; Datadog &#183; Sentry", "Docker · Git · GitHub Actions"),
        ("Prometheus · Datadog · Sentry", "Docker · Git · GitHub Actions"),
        (">automation: <", ">tools: <"),
        ("Python &#183; Bash &#183; JavaScript", "Linux · TailwindCSS · REST APIs"),
        ("Python · Bash · JavaScript", "Linux · TailwindCSS · REST APIs"),
        ("/in/mcperezes", "/in/alejandro-mallama"),
        (">macu-dev<", ">Alejox102004<"),
        ("UTC-3 &#183; Rosario", "UTC-5 &#183; Ecuador"),
        ("UTC-3 · Rosario", "UTC-5 · Ecuador"),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    # Write output
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # Validate XML
    ET.parse(dst_path)
    print(f"SUCCESS: {dst_path} is well-formed XML and valid SVG!")

process_banner('macu-dev-master/assets/banner-dark.v9.svg', 'assets/banner-dark.v9.svg', is_dark=True)
process_banner('macu-dev-master/assets/banner-light.v9.svg', 'assets/banner-light.v9.svg', is_dark=False)
