import streamlit as st
from PIL import Image
import os
import webbrowser

# Theme Colors
themes = {
    "Sunset Glow": "linear-gradient(to right, #ff7e5f, #feb47b)",
    "Ocean Blue": "linear-gradient(to right, #00c6ff, #0072ff)",
    "Emerald Green": "linear-gradient(to right, #11998e, #38ef7d)",
    "Royal Purple": "linear-gradient(to right, #7f00ff, #e100ff)",
    "Fiery Red": "linear-gradient(to right, #ff416c, #ff4b2b)",
    "Golden Hour": "linear-gradient(to right, #ff9a9e, #fad0c4)",
    "Midnight Black": "linear-gradient(to right, #232526, #414345)",
    "Skyline Teal": "linear-gradient(to right, #56ccf2, #2f80ed)"
}

def save_uploaded_file(uploaded_file, folder="uploads"):
    if uploaded_file is not None:
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = os.path.join(folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    return None

def generate_portfolio_page(name, role, theme, image_path, resume_path,
                            schooling, schooling_year, intermediate, intermediate_year,
                            degree, degree_year, schooling_img, intermediate_img, degree_img,
                            services, service_images, projects, project_images):
    with open("generated_portfolio.html", "w") as f:
        f.write(f"""
        <html>
        <head>
            <title>{name}'s Portfolio</title>
            <style>
                body {{
                    background: {themes.get(theme, '#000')};
                    color: white;
                    font-family: Arial, sans-serif;
                    margin:0;
                    padding:0;
                }}
                .navbar {{
                    background-color: #222;
                    padding: 15px;
                    text-align: center;
                }}
                .navbar a {{
                    color: white;
                    text-decoration: none;
                    padding: 10px;
                    font-weight: bold;
                    cursor: pointer;
                }}
                .section {{
                    display: none;
                    padding: 20px;
                }}
                .active {{
                    display: block;
                }}
                .contact-box {{
                    background: rgba(255, 255, 255, 0.2);
                    padding: 20px;
                    border-radius: 10px;
                    display: flex;
                    gap: 20px;
                }}
                .contact-box input, .contact-box textarea, .contact-box button {{
                    width: 100%;
                    padding: 10px;
                    margin: 5px 0;
                    border: none;
                    border-radius: 5px;
                }}
                .contact-box button {{
                    background: #ff416c;
                    color: white;
                    font-size: 16px;
                    cursor: pointer;
                }}
                .grid-container {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 15px;
                    justify-content: center;
                }}
                .grid-container img {{
                    width: 300px;
                    border-radius: 10px;
                    transition: transform 0.3s, box-shadow 0.3s;
                    border: 3px solid white;
                }}
                .grid-container img:hover {{
                    transform: scale(1.05);
                    box-shadow: 0px 0px 15px white;
                }}
                .animation-box {{
                    position: fixed;
                    width: 100px;
                    height: 100px;
                    top: 40%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    animation: blast 1s forwards;
                }}
                @keyframes blast {{
                    0% {{ transform: scale(0.5); opacity: 1; }}
                    100% {{ transform: scale(2); opacity: 0; }}
                }}
                .social-icons {{
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                }}
                .social-icons img {{
                    width: 40px;
                    cursor: pointer;
                }}
                .profile-img {{
                    width: 500px;
                    border-radius: 30px;
                    border: 5px solid white;
                    float: right;
                }}
                .about-img {{
                    border-radius: 50%;
                    width: 150px;
                    margin-right: 20px;
                }}
                .education-grid {{
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 20px;
                    background: rgba(255, 255, 255, 0.1);
                    padding: 15px;
                    border-radius: 10px;
                    text-align: center;
                    clear: both;
                }}
                .education-grid img {{
                    width: 150px;
                    height: 150px;
                    border-radius: 50%;
                    border: 3px solid white;
                }}
                /* Snowflake Animation */
                .snowflakes {{
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    pointer-events: none;
                    z-index: 9999;
                }}
                @keyframes snowfall {{
                    0% {{ transform: translateY(0); }}
                    100% {{ transform: translateY(100vh); }}
                }}
                .snowflake {{
                    position: absolute;
                    top: -10px;
                    width: 10px;
                    height: 10px;
                    background: white;
                    border-radius: 50%;
                    opacity: 0.8;
                    animation: snowfall linear infinite;
                }}
                /* Balloon Effect */
                .balloons {{
                    position: fixed;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    pointer-events: none;
                    z-index: 9998;
                }}
                .balloon {{
                    position: absolute;
                    bottom: -100px;
                    width: 50px;
                    height: 70px;
                    background: radial-gradient(circle, #ff5f6d, #ffc371);
                    border-radius: 50% 50% 0 0;
                    animation: floatBalloon 8s ease-in-out infinite;
                }}
                @keyframes floatBalloon {{
                    0% {{ transform: translateY(0); opacity: 1; }}
                    100% {{ transform: translateY(-120vh); opacity: 0; }}
                }}
                /* Download CV Button Shining Effect */
                .download-cv {{
                    border-radius: 15px;
                    padding: 10px 20px;
                    background: linear-gradient(45deg, #ff416c, #ff4b2b);
                    border: none;
                    color: white;
                    font-size: 16px;
                    cursor: pointer;
                    animation: shine 2s infinite alternate;
                }}
                @keyframes shine {{
                    from {{ box-shadow: 0px 0px 10px white; }}
                    to {{ box-shadow: 0px 0px 20px white; }}
                }}
            </style>
            <script>
                function showSection(sectionId) {{
                    document.querySelectorAll('.section').forEach(section => section.classList.remove('active'));
                    document.getElementById(sectionId).classList.add('active');
                }}
                // Hide snowflakes and balloons after 10 seconds
                setTimeout(() => {{
                    let snowflakes = document.querySelector('.snowflakes');
                    let balloons = document.querySelector('.balloons');
                    if(snowflakes) snowflakes.style.display = 'none';
                    if(balloons) balloons.style.display = 'none';
                }}, 10000);
            </script>
        </head>
        <body>
            <div class="animation-box">&#x1F389;</div>
            <div class="balloons">
                {''.join(f'<div class="balloon" style="left: {i*7}%"></div>' for i in range(10))}
            </div>
            <div class="snowflakes">
                {''.join(f'<div class="snowflake" style="left: {i*5}%"></div>' for i in range(20))}
            </div>
            <div class="navbar">
                <a onclick="showSection('home')">Home</a>
                <a onclick="showSection('about')">About</a>
                <a onclick="showSection('services')">Services</a>
                <a onclick="showSection('projects')">Projects</a>
                <a onclick="showSection('contact')">Contact</a>
            </div>
            <div id="home" class="section active">
                <h1 style="text-align: left; font-size: 40px;">I'm {name}, a passionate {role}</h1>
                <a href="{resume_path}" download><button class="download-cv">Download CV</button></a>
                <br><br>
                <img src="{image_path}" class="profile-img" alt="Profile">
            </div>
            <div id="about" class="section">
                <h2>About Me</h2>
                <div style="display:flex; align-items:center; margin-bottom:20px;">
                    <img src="{image_path}" class="about-img" alt="Student">
                    <p style="font-size:18px; margin:0;">
                        I'm {name}, a passionate {role}. A good employee understands the value of education.
                    </p>
                </div>
                <div class="education-grid">
                    <div><strong>Above Me</strong></div>
                    <div>
                        <img src="{schooling_img}" alt="School">
                        <p>{schooling} ({schooling_year})</p>
                    </div>
                    <div>
                        <img src="{intermediate_img}" alt="Intermediate">
                        <p>{intermediate} ({intermediate_year})</p>
                    </div>
                    <div>
                        <img src="{degree_img}" alt="Degree/BTech">
                        <p>{degree} ({degree_year})</p>
                    </div>
                </div>
            </div>
            <div id="services" class="section">
                <h2>Services</h2>
                <div class="grid-container">
                    {''.join(f'<img src="{service_images[i]}" alt="Service {i+1}">' for i in range(len(services)))}
                </div>
            </div>
            <div id="projects" class="section">
                <h2>Projects</h2>
                <div class="grid-container">
                    {''.join(f'<img src="{project_images[i]}" alt="Project {i+1}">' for i in range(len(projects)))}
                </div>
            </div>
            <div id="contact" class="section">
                <div class="contact-box">
                    <div>
                        <h2>Contact Me</h2>
                        <form>
                            <input type="text" placeholder="Name"><br>
                            <input type="email" placeholder="Enter Email"><br>
                            <textarea placeholder="Message"></textarea><br>
                            <button type="submit">Send</button>
                        </form>
                    </div>
                    <div class="social-icons">
                        <img src="facebook.png" alt="Facebook">
                        <img src="twitter.png" alt="Twitter">
                        <img src="instagram.png" alt="Instagram">
                    </div>
                </div>
            </div>
            <script>
                document.addEventListener("DOMContentLoaded", function() {{
                    let snowflakes = document.querySelectorAll(".snowflake");
                    snowflakes.forEach((flake, index) => {{
                        flake.style.animationDuration = `${{Math.random() * 3 + 2}}s`;
                        flake.style.left = `${{Math.random() * 100}}vw`;
                    }});
                    let balloons = document.querySelectorAll(".balloon");
                    balloons.forEach((balloon, index) => {{
                        balloon.style.animationDuration = `${{Math.random() * 4 + 4}}s`;
                        balloon.style.left = `${{Math.random() * 100}}vw`;
                    }});
                }});
            </script>
        </body>
        </html>
        """)
    webbrowser.open("generated_portfolio.html")

def main():
    st.title("Portfolio Website Generator")
    name = st.text_input("Name of the Student")
    role = st.text_input("Role of the Student")
    theme = st.selectbox("Select a Theme", list(themes.keys()))
    image = st.file_uploader("Upload Profile Image", type=["png", "jpg", "jpeg"], key="home_image")
    resume = st.file_uploader("Upload Resume", type=["pdf", "docx"], key="resume")
    schooling = st.text_input("School Name")
    schooling_year = st.text_input("Year of Passing (School)")
    schooling_img = st.file_uploader("Upload School Image", type=["png", "jpg", "jpeg"], key="school_img")
    intermediate = st.text_input("Intermediate College Name")
    intermediate_year = st.text_input("Year of Passing (Intermediate)")
    intermediate_img = st.file_uploader("Upload Intermediate College Image", type=["png", "jpg", "jpeg"], key="intermediate_img")
    degree = st.text_input("Degree/BTech")
    degree_year = st.text_input("Year of Passing (Degree)")
    degree_img = st.file_uploader("Upload Degree/BTech College Image", type=["png", "jpg", "jpeg"], key="degree_img")
    num_services = st.number_input("Number of Services", min_value=1, step=1)
    services = [st.text_input(f"Service {i+1}", key=f"service_{i}") for i in range(num_services)]
    service_images = [save_uploaded_file(st.file_uploader(f"Upload Image for {services[i]}", type=["png", "jpg", "jpeg"], key=f"service_img_{i}")) for i in range(num_services)]
    num_projects = st.number_input("Number of Projects", min_value=1, step=1)
    projects = [st.text_input(f"Project {i+1}", key=f"project_{i}") for i in range(num_projects)]
    project_images = [save_uploaded_file(st.file_uploader(f"Upload Image for {projects[i]}", type=["png", "jpg", "jpeg"], key=f"project_img_{i}")) for i in range(num_projects)]
    if st.button("Generate Website"):
        generate_portfolio_page(
            name, role, theme,
            save_uploaded_file(image), save_uploaded_file(resume),
            schooling, schooling_year, intermediate, intermediate_year, degree, degree_year,
            save_uploaded_file(schooling_img), save_uploaded_file(intermediate_img), save_uploaded_file(degree_img),
            services, service_images, projects, project_images
        )
        st.success("Website Generated Successfully! Opening in new tab...")

if __name__ == "__main__":
    main()
