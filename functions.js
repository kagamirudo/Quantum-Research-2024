const LOCAL = '/';
const REPO = 'https://kagamirudo.github.io/Quantum-Research-2024/'
const API = 'https://api.github.com/repos/kagamirudo/Quantum-Research-2024/commits';
const BASE_URL = window.location.hostname === 'localhost' ? LOCAL : REPO;

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

async function listBlog() {
    const weeks = Array.from({ length: 32 }, (_, i) => i + 1);
    const blogList = document.querySelector('.blog-list');
    const availableWeeks = [];

    // First: Collect all weeks that exist
    for (const week of weeks) {
        const formattedWeek = week < 10 ? `0${week}` : `${week}`;
        const weekFolder = `Week ${formattedWeek}`;
        try {
            const response = await fetch(`${BASE_URL}${weekFolder}/`, { method: 'HEAD' });
            if (response.ok) {
                availableWeeks.push(week);  // Only push if folder exists
            } else {
                console.log(`Folder for Week ${formattedWeek} does not exist README. Continuing...`);
            }
        } catch (error) {
            console.error('Error fetching folder:', error);
        }
    }

    // Second: After collecting, render in order
    availableWeeks.sort((a, b) => a - b);
    for (const week of availableWeeks) {
        const formattedWeek = week < 10 ? `0${week}` : `${week}`;
        const li = document.createElement('li');
        const a = document.createElement('a');
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
    }
}


async function fetchMarkdown(file) {
    console.log(BASE_URL);
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

function loadReferences() {
    const referencesList = document.querySelector('.references-list');
    if (!referencesList) return;

    // Add link to external CSS file
    if (!document.querySelector('link[href="references.css"]')) {
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'references.css';
        document.head.appendChild(link);
    }

    // Add header for references section
    const header = document.createElement('h2');
    header.textContent = 'References';
    header.className = 'references-header';
    referencesList.appendChild(header);

    const references = [
        {
            title: "Tower: Data Structures in Quantum Superposition",
            authors: "Yuan, C., & Carbin, M.",
            year: "2022",
            link: "https://arxiv.org/abs/2205.10255",
            content: "Discusses quantum data structures and memory allocation techniques, introduces Core Tower language for quantum programming, and covers Boson memory allocator for quantum memory management."
        },
        {
            title: "A quantum algorithm for finding the minimum",
            authors: "Dürr, C., & Høyer, P.",
            year: "1996",
            link: "https://arxiv.org/abs/quant-ph/9607014",
            content: "Introduces quantum minimum-finding algorithm, used in LMSR implementation for efficient search, provides O(√n) complexity for finding minimum values."
        },
        {
            title: "Rapid solution of problems by quantum computation",
            authors: "Deutsch, D., & Jozsa, R.",
            year: "1992",
            link: "https://doi.org/10.1098/rspa.1992.0167",
            content: "One of the first quantum algorithms demonstrating quantum advantage, shows exponential speedup for specific problems, foundation for understanding quantum parallelism."
        },
        {
            title: "A fast quantum mechanical algorithm for database search",
            authors: "Grover, L. K.",
            year: "1996",
            link: "https://arxiv.org/abs/quant-ph/9605043",
            content: "Introduces Grover's algorithm for quantum search, provides quadratic speedup over classical search, used in LMSR implementation for efficient rotation comparison."
        },
        {
            title: "Quantum walk algorithm for element distinctness",
            authors: "Ambainis, A.",
            year: "2007",
            link: "https://arxiv.org/abs/quant-ph/0311001",
            content: "Discusses quantum algorithms for element distinctness, introduces quantum walk techniques, relevant for quantum data structure traversal."
        },
        {
            title: "A linear algorithm for perfect matching in hexagonal systems",
            authors: "Hansen, P., & Zheng, M.",
            year: "1993",
            link: "https://www.sciencedirect.com/science/article/pii/0012365X93902944",
            content: "Proposes a linear algorithm for finding perfect matchings in hexagonal systems, improving upon previous methods' complexity."
        },
        {
            title: "Testing for the consecutive ones property, interval graphs, and graph planarity using PQ-tree algorithms",
            authors: "Booth, K. S., & Lueker, G. S.",
            year: "1976",
            link: "https://www.sciencedirect.com/science/article/pii/S0022000076800451",
            content: "Introduces PQ-tree algorithms for graph theory applications, foundational for understanding graph structures in quantum computing contexts."
        },
        {
            title: "Chemical graph theory: Benzenoid hydrocarbons and graph invariants",
            authors: "Balaban, A. T., & Klein, D. J.",
            year: "1985",
            link: "https://doi.org/10.1021/ci00047a001",
            content: "Presents fundamental concepts in chemical graph theory, focusing on Benzenoid hydrocarbons and their graph-theoretical properties."
        },
        {
            title: "Kekulé structures in benzenoid hydrocarbons",
            authors: "Cyvin, S. J., & Gutman, I.",
            year: "1988",
            link: "https://link.springer.com/book/10.1007/978-3-662-00892-8",
            content: "Comprehensive study of Kekulé structures in benzenoid hydrocarbons, essential for understanding molecular structures in quantum computing applications."
        },
        {
            title: "IBM Quantum Experience Documentation",
            link: "https://quantum-computing.ibm.com/docs/",
            content: "Provides implementation details for quantum circuits, covers quantum gate operations and measurements, includes practical examples of quantum algorithms."
        },
        {
            title: "Quantum Computing Research Overview",
            authors: "Boady, M., & Pham, G.",
            year: "2024",
            link: "https://github.com/kagamirudo/Quantum-Research-2024",
            content: "Current research on applying Grover's algorithm to LMSR, implementation details for Benzenoid system classification, analysis of quantum algorithms for combinatorial search."
        }
    ];

    references.forEach(ref => {
        const refElement = document.createElement('div');
        refElement.className = 'reference-item';

        let authorsText = ref.authors ? `${ref.authors}. ` : '';
        let yearText = ref.year ? `(${ref.year}). ` : '';
        let linkText = ref.link ? `<a href="${ref.link}" target="_blank" rel="noopener noreferrer">${ref.title}</a>` : ref.title;

        refElement.innerHTML = `
            <div class="reference-header">
                <h3>${authorsText}${yearText}${linkText}</h3>
            </div>
            <div class="reference-content">
                <p>${ref.content}</p>
            </div>
        `;
        referencesList.appendChild(refElement);
    });
}

function initBlog() {
    getLastGitPushDate();
    // Initialize components independently
    if (document.querySelector('.blog-list')) {
        listBlog();
    }
    if (document.querySelector('.references-list')) {
        loadReferences();
    }
}

// Call the init function when the document is ready
document.addEventListener('DOMContentLoaded', initBlog);
