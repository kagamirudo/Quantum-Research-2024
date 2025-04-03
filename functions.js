const BASE_URL = '/';
const REPO = 'https://github.com/kagamirudo/Quantum-Research-2024/'
const API = 'https://api.github.com/repos/kagamirudo/Quantum-Research-2024/commits'

function getLastGitPushDate() {
    fetch(API)
        .then(response => response.json())
        .then(data => {
            const lastCommitDate = new Date(data[0].commit.author.date);
            document.getElementById('publish-date').textContent =
                `${lastCommitDate.toLocaleDateString('en-US',
                    {
                        weekday: 'short',
                        year: 'numeric',
                        month: 'short',
                        day: 'numeric'
                    }
                )}`;
        });
}

function listBlog() {
    const weeks = Array.from({ length: 16 }, (_, i) => i + 1);
    const blogList = document.querySelector('.blog-list');
    weeks.forEach(week => {
        const formattedWeek = week < 10 ? `0${week}` : week;
        const weekFolder = `Week ${formattedWeek}`;
        fetch(`${weekFolder}/`, { method: 'HEAD' })
            .then(response => {
                if (response.ok) {
                    const li = document.createElement('li');
                    const a = document.createElement('a');
                    // a.href = `${weekFolder}/README.md`;
                    a.href = '#';
                    a.textContent = `Week ${formattedWeek}`;
                    a.onclick = async () => {
                        try {
                            await fetchMarkdown(`Week ${formattedWeek}/README.md`);
                        } catch (error) {
                            console.log(`README.md not found for Week ${formattedWeek}.`);
                        }
                    };
                    li.appendChild(a);
                    blogList.appendChild(li);
                } else {
                    console.log(`Folder for Week ${formattedWeek} does not exist. Continuing...`);
                }
            })
            .catch(error => console.error('Error fetching folder:', error));
    });
}

async function fetchMarkdown(file) {
    const BASE_URL = window.location.hostname === 'localhost' ? '' : REPO;
    try {
        if (typeof marked === 'undefined') {
            throw new Error('Marked library is not loaded. Please include the marked.js library.');
        }
        const fullUrl = `${BASE_URL}${file}`;
        console.log('Fetching from:', fullUrl);
        const response = await fetch(fullUrl);
        if (!response.ok) {
            throw new Error(`Failed to fetch markdown (${response.status} ${response.statusText})`);
        }
        const markdown = await response.text();
        const markdownBody = document.querySelector('.markdown-body');
        if (!markdownBody) {
            throw new Error('Markdown container not found');
        }
        markdownBody.innerHTML = marked.parse(markdown);
        if (typeof renderMathInElement === 'function') {
            renderMathInElement(markdownBody);
        }
    } catch (error) {
        console.error('Error fetching markdown:', error);
        const markdownBody = document.querySelector('.markdown-body');
        if (markdownBody) {
            markdownBody.innerHTML = `<div class="error-message">
                <h2>Content Not Available</h2>
                <p>The requested content could not be loaded.</p>
                <p>Error: ${error.message}</p>
            </div>`;
        }
    }
}

function loadBlogPosts() {
    const blogListElement = document.querySelector('.blog-list');
    const posts = [
        { title: "First Blog Post", content: "This is the content of the first blog post." },
        { title: "Second Blog Post", content: "This is the content of the second blog post." }
    ];

    posts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.classList.add('blog-post');
        postElement.innerHTML = `<h2>${post.title}</h2><p>${post.content}</p><br>`;
        blogListElement.appendChild(postElement);
    });
}

function initBlog() {
    getLastGitPushDate();
    loadBlogPosts();
    listBlog();
}

// Call the init function when the document is ready
document.addEventListener('DOMContentLoaded', initBlog);
