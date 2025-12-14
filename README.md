# Commit Intelligence Analyzer

A comprehensive web application for analyzing GitHub repository commit patterns, contributor activity, and code quality metrics.

## Features

- **Repository Analysis**: Analyze any public GitHub repository
- **Commit Pattern Analysis**: Categorize commits by type (feature, bugfix, refactor, etc.)
- **Contributor Insights**: Track contributor activity and collaboration patterns
- **Temporal Analysis**: Analyze commit patterns over time, by hour, day, and month
- **File Analysis**: Identify most changed files and file type distributions
- **Code Quality Metrics**: Assess code quality based on commit patterns
- **Interactive Visualizations**: Multiple chart types for data exploration

## Project Structure

```
commit-intelligence-analyzer/
│── app.py                 # Main Flask application
│── github_api.py          # GitHub API integration
│── analyzer.py            # Commit analysis logic
│── visualizer.py          # Data visualization
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd commit-intelligence-analyzer
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Enter a GitHub repository URL (e.g., `https://github.com/owner/repo`)

4. Optionally provide a GitHub token for higher rate limits

5. Click "Analyze" to view comprehensive repository insights

## API Endpoints

- `GET /` - Main application interface
- `POST /analyze` - Analyze repository commits
- `GET /health` - Health check endpoint

## Analysis Features

### Commit Analysis
- Total commits, additions, deletions
- Average commit size
- Commit type categorization
- Temporal patterns (hourly, daily, weekly, monthly)

### Contributor Analysis
- Top contributors by activity
- Contribution distribution
- Collaboration patterns
- Author-specific metrics

### File Analysis
- Most changed files
- File extension distribution
- File type categorization
- Collaboration on specific files

### Code Quality Metrics
- Quality scoring based on commit patterns
- Large commit identification
- Revert pattern analysis
- Activity metrics

## Dependencies

- **Flask 2.3.3**: Web framework
- **requests 2.31.0**: HTTP client for GitHub API
- **python-dateutil 2.8.2**: Date parsing utilities
- **numpy 1.24.3**: Numerical computations
- **pandas 1.5.3**: Data manipulation

## GitHub API Rate Limits

- **Without token**: 60 requests per hour
- **With token**: 5,000 requests per hour

To use a GitHub token:
1. Generate a personal access token on GitHub
2. Enter it in the application when prompted
3. Token is only used for API requests and not stored

## Configuration

The application can be configured through environment variables:

- `FLASK_ENV`: Set to `development` for debug mode
- `FLASK_PORT`: Port number (default: 5000)
- `FLASK_HOST`: Host address (default: 0.0.0.0)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Troubleshooting

### Common Issues

1. **GitHub API Rate Limit**: Use a GitHub token for higher limits
2. **Private Repositories**: Ensure token has proper permissions
3. **Large Repositories**: Analysis may take time for repositories with many commits

### Error Handling

The application includes comprehensive error handling for:
- Invalid repository URLs
- GitHub API errors
- Network connectivity issues
- Data parsing errors

## Future Enhancements

- [ ] Frontend UI improvements
- [ ] Additional visualization types
- [ ] Repository comparison features
- [ ] Export functionality
- [ ] Caching for improved performance
- [ ] Authentication system
- [ ] Database integration for storing analyses
