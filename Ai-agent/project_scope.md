Acceptance criteria
Functionality:

A website that allows users to view, create, edit, and delete blog posts.
Each blog post has a title, content, author, and timestamp.
Users can navigate between posts using pagination or “Next/Previous” buttons.
Optional: Users can comment on posts.

Technical Requirements:

Use Python with Flask or Django for the backend.
Use a relational database (SQLite, PostgreSQL, or MySQL) to store posts and comments.
Use HTML, CSS, and JavaScript for the frontend.
Implement server-side rendering for post listing and details.
Add form validation for creating and editing posts.
Use templates for reusable UI components (header, footer, navigation).
Optional: Add a search feature to find posts by title or content.

Navigation & User Experience:

Users can click Next or Previous to navigate through posts.
Display recent posts on the homepage.
Optionally, show a sidebar with popular posts or categories.

Testing & Quality:

Include unit tests for backend logic (CRUD operations).
Include integration tests for routes and templates.
Ensure security best practices: input sanitization, CSRF protection, XSS prevention.

Optional Advanced Features:

User authentication: Users can sign up, log in, and manage their posts.
Markdown support for post content.
Likes or upvotes for posts.
REST API endpoints to fetch posts programmatically.
