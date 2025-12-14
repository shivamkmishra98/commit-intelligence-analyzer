import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Commit Intelligence Analyzer",
    layout="wide"
)

st.title("📊 Commit Intelligence Analyzer")
st.caption("Analyze GitHub commit behavior using Streamlit")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("🔗 Repository Input")

    repo_url = st.text_input(
        "GitHub Repository URL",
        placeholder="https://github.com/owner/repo"
    )

    token = st.text_input(
        "GitHub Token (recommended)",
        type="password"
    )

    st.info(
        "⚠️ GitHub allows only 60 requests/hour without token.\n"
        "Using a token increases limit to 5000/hour."
    )

    analyze_btn = st.button("🚀 Analyze Repository")

# ---------------- FUNCTIONS ----------------
@st.cache_data(show_spinner=False)
def fetch_commits(owner, repo, token):
    """Fetch all commits using pagination"""
    commits = []
    page = 1

    headers = {"Authorization": f"token {token}"} if token else {}

    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        params = {"per_page": 100, "page": page}

        response = requests.get(url, headers=headers, params=params)

        # Rate limit handling
        if response.status_code == 403:
            raise Exception(
                "GitHub API rate limit exceeded. "
                "Please add a GitHub Personal Access Token."
            )

        response.raise_for_status()
        data = response.json()

        if not data:
            break

        commits.extend(data)
        page += 1

    return commits


def analyze_commits(commits):
    rows = []
    for c in commits:
        commit = c["commit"]
        rows.append({
            "date": commit["author"]["date"],
            "message": commit["message"]
        })

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df["hour"] = df["date"].dt.hour
    df["weekday"] = df["date"].dt.day_name()

    stats = {
        "total_commits": len(df),
        "active_days": df["date"].dt.date.nunique(),
        "avg_commits": round(len(df) / df["date"].dt.date.nunique(), 2),
        "most_active_hour": int(df["hour"].mode()[0])
    }

    return df, stats


def plot_bar(series, title, xlabel):
    fig, ax = plt.subplots()
    series.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Commits")
    st.pyplot(fig)


# ---------------- MAIN LOGIC ----------------
if analyze_btn:
    if not repo_url:
        st.error("❌ Repository URL is required")
        st.stop()

    try:
        parts = repo_url.strip("/").split("/")
        if len(parts) < 2:
            st.error("❌ Invalid GitHub repository URL")
            st.stop()

        owner, repo = parts[-2], parts[-1]

        with st.spinner("🔄 Fetching commits from GitHub..."):
            commits = fetch_commits(owner, repo, token)

        with st.spinner("📊 Analyzing commit data..."):
            df, stats = analyze_commits(commits)

        st.success("✅ Analysis completed successfully")

        # ---------------- METRICS ----------------
        st.subheader("📌 Key Metrics")
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Commits", stats["total_commits"])
        col2.metric("Active Days", stats["active_days"])
        col3.metric("Avg Commits / Day", stats["avg_commits"])
        col4.metric("Most Active Hour", f'{stats["most_active_hour"]}:00')

        # ---------------- VISUALS ----------------
        st.subheader("📈 Commit Activity")

        col1, col2 = st.columns(2)

        with col1:
            plot_bar(
                df["hour"].value_counts().sort_index(),
                "Commits by Hour",
                "Hour of Day"
            )

        with col2:
            plot_bar(
                df["weekday"].value_counts(),
                "Commits by Weekday",
                "Day"
            )

        # ---------------- MESSAGE INSIGHTS ----------------
        st.subheader("📝 Commit Message Insights")
        avg_len = int(df["message"].str.len().mean())
        st.write(f"Average commit message length: **{avg_len} characters**")

        with st.expander("📄 Sample Commit Messages"):
            st.write(df["message"].head(10))

    except Exception as e:
        st.error(f"🚨 Error: {e}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with Python & Streamlit | DevOps Analytics Project")
