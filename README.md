# Langchain Github Profiler Analyzer

This repository contains a **GitHub User Profile Analyzer** that leverages **LangChain, OpenAI, and DuckDuckGo** to generate an **informative markdown profile** for a GitHub user. The script fetches user data from the **GitHub API**, enhances it with **DuckDuckGo search results**, and processes the information using **GPT-4o-mini**.

## 🚀 Features

-   **Fetch GitHub user details** (name, followers, repositories, profile picture, etc.).
-   **Enhance data with DuckDuckGo search results** for a broader online presence.
-   **Generate a structured markdown profile** with OpenAI’s **GPT-4o-mini**.
-   **Store debug results in JSON** for easier troubleshooting.

## 📌 How It Works

1. **User inputs a GitHub username.**
2. **The script fetches GitHub API data** (followers, repositories, etc.).
3. **DuckDuckGo search enhances the profile** with external links & references.
4. **LangChain processes the data** to generate a **detailed markdown summary**.
5. **Output is printed & stored** for further use.

## 🛠️ Technologies Used

-   **Python**
-   **LangChain** (for structured data processing)
-   **OpenAI API** (for GPT-based text generation)
-   **DuckDuckGo Search API** (for external data enrichment)
-   **GitHub API** (to fetch user details)

## 🔧 Setup

1. Clone the repository:
    ```bash
    git clone git@github.com:AlgoMart/langchain-github-profile-analyzer.git
    cd langchain-github-profile-analyzer
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up OpenAI API key in `.env`:
    ```
    OPENAI_API_KEY=your_api_key
    ```
4. Run the script:
    ```bash
    python main.py
    ```

## 📚 Use Cases

-   Automated **GitHub profile summarization**
-   **Recruitment & hiring insights** for developers
-   **Portfolio enhancement** for GitHub users
-   **Tech influencer analysis**

### ⭐ Star the repo if you find it useful! 🚀

---

# Example Markdown

# Yash Jain

![Yash Jain](https://avatars.githubusercontent.com/u/44037814?v=4)

## Profile Overview

-   **Name:** Yash Jain
-   **GitHub Username:** [yash0307jain](https://github.com/yash0307jain)
-   **Followers:** 21
-   **Following:** 8
-   **Repositories:** 37
-   **Description:** Senior Backend & AI Engineer based in Bangalore. Passionate about building scalable systems and exploring AI technologies.

## Online Presence

-   **[Threads Profile](https://www.threads.net/@bokucandraw_)**: Engaging with a community of 3.8K followers, sharing art and tutorials.
-   **[Instagram Post](https://www.instagram.com/p/DFNWlY9sxXx/)**: A glimpse into personal interests and creativity.
-   **[GitHub Gist - VSCode Settings](https://gist.github.com/yash0307jain/25cc0daa507eb48f060ea96cf1e2c298)**: A collection of settings for Visual Studio Code, showcasing coding preferences and configurations.
-   **[Personal Website](https://yashjain14.github.io/)**: A portfolio highlighting projects and academic background, currently pursuing a double bachelor's in Computer Science and Business at Nanyang Technological University.

## Skills & Interests

-   **Backend Development**: Expertise in building robust backend systems.
-   **Artificial Intelligence**: Passionate about exploring AI technologies and their applications.
-   **Scalability**: Focused on creating systems that can efficiently scale with user demand.

## Connect with Yash

Feel free to reach out or follow Yash on GitHub and other platforms to stay updated on his latest projects and contributions!
