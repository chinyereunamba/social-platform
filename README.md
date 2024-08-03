
# Social Media Platform

This is a full-stack social media platform built using Django and Django REST Framework for the backend, with HTML, CSS, and JavaScript for the frontend. The platform includes user authentication, profile management, posting, following, liking, commenting, real-time notifications, and direct messaging.

## Key Features

### User Authentication and Profile Management
- Sign-up, login, and logout functionality.
- Profile creation and editing.
- Profile pictures and bio.

### Following/Followers Functionality
- Ability to follow and unfollow users.
- Display of followers and following lists.

### Post Creation, Liking, and Commenting
- Users can create text, image, or video posts.
- Like and unlike posts.
- Add comments to posts.

### Real-Time Notifications
- Notifications for new followers, likes, and comments.
- Real-time updates using Django Channels and WebSockets.

### Direct Messaging System
- Real-time private messaging between users.
- Message history and notifications for new messages.
- Seen/unseen status for messages.

## Implementation Steps

1. **Set Up Django Project**
   - Create a new Django project and app.
   - Configure settings, including database setup.

2. **User Authentication**
   - Use Django's built-in authentication system or Django Allauth.
   - Implement sign-up, login, logout, and password reset functionalities.
   - Create profile models linked to the user model with additional fields like profile picture and bio.

3. **Profile Management**
   - Create views and templates for user profiles.
   - Allow users to edit their profiles and upload profile pictures.

4. **Follow System**
   - Implement a follow model to handle follower relationships.
   - Create views and templates to follow and unfollow users.
   - Display followers and following lists on user profiles.

5. **Post Functionality**
   - Create a post model with fields for content, image, and video.
   - Implement views and templates for creating, editing, and deleting posts.
   - Display posts on user profiles and a feed of posts from followed users.

6. **Like and Comment System**
   - Implement a like model to track likes on posts.
   - Create views and templates to like and unlike posts.
   - Implement a comment model and views to add comments to posts.

7. **Real-Time Notifications**
   - Use Django Channels to implement WebSocket connections.
   - Create a notification model to store notifications.
   - Implement views to display notifications in real-time.

8. **Direct Messaging**
   - Implement a messaging model to store private messages.
   - Use Django Channels for real-time messaging.
   - Create views and templates for the messaging interface.
   - Add notifications for new messages and seen/unseen status.

9. **Testing and Deployment**
   - Write unit tests for all major functionalities.
   - Ensure the app is responsive and works well on various devices.
   - Deploy the app to a hosting service like Heroku or DigitalOcean.

## Technologies and Tools

- **Frontend**: HTML, CSS, JavaScript, Bootstrap or Tailwind CSS.
- **Backend**: Django, Django REST Framework for API endpoints.
- **Database**: PostgreSQL or SQLite for local development.
- **Real-Time Communication**: Django Channels, WebSockets.
- **Authentication**: Django Allauth or Django's built-in authentication system.
- **Deployment**: Heroku, DigitalOcean, or another hosting service.
