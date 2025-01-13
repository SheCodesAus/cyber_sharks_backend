# Product Name - To Be Confirmed

# Table of Contents

[Mission Statement](#mission-statement)

[Features](#features)
- [Summary](#summary)
- [Users](#users)
- [Collections](#collections)
- [Pages/Endpoint Functionality](#pagesendpoint-functionality)
- [Nice To Haves](#nice-to-haves)

[Technical Implementation](#technical-implementation)
- [Back-End](#back-end)
- [Front-End](#front-end)
- [Git & Deployment](#git--deployment)

[Target Audience](#target-audience)
- [User Personas](#user-personas)
- [User Stories](#user-stories)

[Back-end Implementation](#back-end-implementation)
- [API Specification](#api-specification)
- [Database Schema](#database-schema)

[Front-end Implementation](#front-end-implementation)
- [Wireframes](#wireframes)
  - [Design Inspiration](#design-inspiration)
  - [Wireframes - Version 1](#wireframes---version-1)
  - [Wireframe - HOME](#wireframe---home)
  - [Wireframe - LOGIN](#wireframe---login)
  - [Wireframe - SIGNIN](#wireframe---signin)
  - [Wireframe - SHOWING RESULTS](#wireframe---showing-results)
  - [Wireframe - PROFILE](#wireframe---profile)
  - [Wireframe - CREATE PROFILE](#wireframe---create-profile)
  - [Wireframe - ERROR PAGE](#wireframe---error-page)
  - [Wireframe - PAGE NO RESULT](#wireframe---page-no-result)

[Style Guide](#style-guide)
- [Option 1: AESOP Style](#option-1-aesop-style)
  - [Typography](#typography)
  - [Color Palette](#color-palette)
  - [Interactive Elements](#interactive-elements)
- [Option 2: Sunroom Style](#option-2-sunroom-style)
  - [Typography](#typography-1)
  - [Color Palette](#color-palette-1)
  - [Interactive Elements](#interactive-elements-1)
- [Option 3: Hinge Style](#option-3-hinge-style)
  - [Typography](#typography-2)
  - [Color Palette](#color-palette-2)
  - [Interactive Elements](#interactive-elements-2)
- [Icons](#icons)
  - [Common Icons Used](#common-icons-used)


## Mission Statement

Empowering growth by connecting role models and opportunities in tech through a platform for collaboration and inclusivity.

## Features

### Summary
The web app will connect diverse individuals to panels and speaking opportunities by allowing:
- Profiles for speakers to showcase their experience and expertise
- Organizers to search and filter profiles effectively
- A user-friendly platform that balances accessibility and professionalism

### Users

| Type | Access | Role Type Assignment |
|------|---------|---------------------|
| Superuser/Admin | - Login, logout, and full profile management<br>- Verify and delete inactive profiles<br>- Update platform content<br>- Manage user accounts<br>- Access admin dashboard | Platform managers and administrators |
| Individual User | - Create and update personal profiles<br>- Claim or request profile deletion<br>- Login and logout<br>- Filter and search profiles | Role models, diverse professionals seeking opportunities |
| Guest User | - View profiles<br>- Search profiles but cannot contact without an account | Event organizers and general users exploring profiles |

### Collections

| Feature | Access | Notes/Conditions |
|---------|---------|-----------------|
| Profile Information | Admin, User | Name, title, role, specialization, experience levels (technical and speaking), location, bio, and contact |
| Profile Management | Admin, User | Profiles can be created by individuals or by nomination. Inactivity may lead to automatic deactivation |
| Search and Filter | Guests, Admin, User | Filter by specialization, location, experience levels |
| Profile Claiming | Admin, User | Users can claim a profile if created by someone else. Stretch goal for MVP |

### Pages/Endpoint Functionality

| Endpoint/Page | Functionality | Comments |
|--------------|---------------|-----------|
| Homepage | - Introduction to the platform<br>- Create profile<br>- Carousel of featured profiles<br>- Search and filter functionality | Responsive design for desktop-first users |
| Profiles | - Individual profiles with detailed information<br>- Continuous scroll for browsing profiles<br>- Search and filter functionality | Key feature of the MVP |
| Profile | - Display detailed speaker information<br>- Provide a "Contact Speaker" option (requires login)<br>- Allow users to search and filter profiles<br>- Allow guests to view profiles but restrict contacting | Key feature of the MVP. Profiles are searchable and filterable |
| Create profile | - Provide a form for users to input their details<br>- Allow admins to create or edit profiles for others<br>- Save profiles to the database<br>- Validate inputs | Users can update their profiles after creation |
| Signup Page | - Enable new user registration<br>- Validate email format and passwords<br>- Include CAPTCHA (optional)<br>- Redirect users to create profile | Email should be mandatory to activate an account |
| Admin Dashboard | - Manage all user and profile data<br>- Delete inactive profiles | Admin access only |
| Login/Signup | - Create accounts<br>- Manage login/logout | Required for contacting profiles |
| Profile Management | - Users can create and update their profiles<br>- Admin can verify or delete profiles | Separate profile creation from account creation |

### Nice To Haves

- Profile likes and connection counts
- Animations for improved user experience
- Responsive design for mobile use
- Claim profiles feature
- Allow guests to view profiles without contact access

## Technical Implementation

### Back-End

- Django / DRF API
- Python

### Front-End

- React / JavaScript
- HTML/CSS

### Git & Deployment
- Heroku
- Netlify
- GitHub

This application's back-end will be deployed to Heroku. The front-end will be deployed separately to Netlify.
 
We will also use Insomnia to ensure API endpoints are working smoothly (we will utilise a local and deployed environment in Insomnia).

## Target Audience

Our platform serves two primary audience segments:

**Primary Audience:**
- Event organisers in the tech industry looking for women speakers and role models in tech
- Women in tech or transitioning into tech roles, seeking speaking opportunities, and expand their network
- Students and minority folks looking for inspiration and role models

**Secondary Audience:**
- Professionals seeking to build their personal brand and expand their professional network
- Students and early career professionals exploring tech career paths

### User Personas
| Persona | Name | Occupation | Goals | Challenges | Preferred Features | Quote |
|---------|------|------------|--------|------------|-------------------|--------|
| Guest/Student/Community Member | Priya Kapoor, 24 | Software Engineering Student | • Discover relatable role models in tech.<br>• Learn about different career paths and specialisations.<br>• Build confidence in pursuing a tech career. | • Lack of access to diverse representation in the tech industry.<br>• Uncertainty about which specialisation to pursue. | • Browse functionality for profiles and success stories.<br>• Insights into career paths.<br>• Role models with relatable journeys. | *"I want to explore tech career options and find role models who inspire me."* |
| Speaker/Role Model | Emily Carter, 37 | AI Research Scientist | • Build a personal brand as an expert in the tech industry.<br>• Inspire and mentor women in tech.<br>• Be discovered for speaking opportunities. | • Limited time to manage outreach opportunities.<br>• Difficulty showcasing expertise effectively online. | • Profile creation and editing tools.<br>• Privacy controls for contact preferences.<br>• Easy-to-use interface for highlighting expertise. | *"I want to inspire others while continuing to grow my professional network."* |
| Event Organiser | Camila Smith, 42 | Event Coordinator at TechTechy | • Find diverse, qualified speakers for tech events.<br>• Streamline the speaker selection process.<br>• Ensure a professional and engaging event experience. | • Difficulty finding speakers with specific expertise.<br>• Limited time for manual searches and outreach. | • Advanced search filters (e.g., expertise, location).<br>• Detailed speaker profiles with professional backgrounds.<br>• Contact tools for outreach | *"I want to ensure our events feature speakers who inspire and engage the audience."* |

### User Stories
# User Stories, Requirements, and Acceptance Criteria

## FIRST LEVEL USER - ALL USERS

| **User Type** | **User Stories**                                                                                     | **Requirements**                                                                                                                      | **Acceptance Criteria**                                                                                                                                                      |
|---------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Guest**     | As a guest, I want to discover diverse role models in tech so that I can be inspired about potential career paths. | - Browse functionality<br>- Featured speaker portfolios<br>- Success stories<br>- Career path visibility                           | - Can browse speaker portfolios freely<br>- Can find relatable speaker portfolios<br>- Can see diverse representations<br>- Can view career journeys                         |
| **Guest**     | As a guest, I want to sign up easily so that I can personalize my experience and access premium features like direct contact. | - Clear registration form<br>- Required fields validation<br>- Privacy policy acceptance<br>- Clear indication of mandatory fields | - Can create an account with name, email, and password<br>- Can fill in all required profile fields<br>- Sees validation errors in real-time<br>- Can accept terms and privacy policy<br>- Can complete registration process in under 5 minutes<br>- Automatically logs in after successful registration<br>- Can access previously restricted features after signup |

## SECOND LEVEL USER - LOGGED IN USERS

| **User Type** | **User Stories**                                                                                     | **Requirements**                                                                                                                      | **Acceptance Criteria**                                                                                                                                                      |
|---------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Speaker**   | As a speaker, I want to create and manage speaker portfolio(s) so that event organisers can find me for speaking opportunities. | - Registration functionality<br>- Speaker portfolio(s) creation form<br>- Speaker portfolio(s) editing capability<br>- Required fields validation | - Can create account<br>- Can edit speaker portfolio(s)<br>- Can view own speaker portfolio(s)<br>- Can fill all required fields                                           |
| **Speaker**   | As a speaker, I want to manage my contact preferences so that I can be reached appropriately.        | - Contact details input<br>- Privacy settings<br>- LinkedIn integration<br>- Contact form preferences                               | - Can set preferred contact method<br>- Can link professional speaker portfolio(s)<br>- Can update contact info<br>- Can control visibility                                 |
| **Speaker**   | As a speaker, I want to delete my speaker portfolio(s) so that I can remove my information from the platform if I'm no longer available for speaking opportunities. | - Speaker portfolio(s) deletion functionality<br>- Confirmation process / deletion alert<br>- Data removal notification             | - Can initiate speaker portfolio(s) deletion<br>- Must confirm deletion action<br>- All personal data is removed<br>- Cannot be found in search results after deletion<br>- Can still stay signed in to visit others' speaker portfolios and create one again if needed |
| **Event Organiser** | As an event organiser, I want to contact potential speakers so that I can discuss speaking opportunities. | - Contact Buttons<br>- Contact mechanism<br>- Professional messaging<br>- Contact privacy<br>- Response tracking                    | - Can initiate contact/reach out to users via LinkedIn or email<br>- Can send professional inquiries<br>- Can track outreach<br>- Can follow up                            |
| **Event Organiser** | As an event organiser, I want to search for speakers based on specific criteria so that I can find appropriate speakers for my events. | - Search functionality<br>- Multiple filter options: Name & Location<br>- Experience level filtering                                | - Can easily access search function<br>- Can search by name and location<br>- Can filter by expertise<br>- Can combine search criteria<br>- Can view search results        |
| **Event Organiser** | As an event organiser, I want to browse speaker portfolio(s) so that I can evaluate their suitability for my event. | - Speaker portfolio(s) viewing capability<br>- Detailed information display<br>- Professional background<br>- Speaking history      | - Can view complete speaker portfolio(s)<br>- Can see all relevant info                                                                                                    |
| **Speaker/Event Organiser** | As a Speaker/Event Organiser, I want to delete my account so that I can remove all my speaker portfolio(s) and information from the platform if I'm no longer interested in speaking opportunities. | - Account deletion functionality<br>- Deletion confirmation steps<br>- Warning about data loss                                      | - Can initiate account deletion from account settings<br>- Must acknowledge permanent data loss warning<br>- Can see list of all data to be deleted (speaker portfolios, messages, etc.)<br>- All associated speaker portfolio(s) are removed<br>- All contact information is removed<br>- Cannot log in after grace period expires |

## THIRD LEVEL USER - ADMIN

| **User Type** | **User Stories**                                                                                     | **Requirements**                                                                                                                      | **Acceptance Criteria**                                                                                                                                                      |
|---------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Admin**     | As an admin, I want to manage and moderate content so that the platform maintains high quality and professionalism. | - Speaker portfolio(s) deletion functionality<br>- Speaker portfolio(s) editing capability<br>- Account deletion functionality<br>- Account editing capability<br>- Speaker portfolio(s) creation form<br>- User creation form | - Can manage speaker portfolio(s): View, Create, Edit, Delete<br>- Can manage accounts: View, Create, Edit, Delete<br>- Can maintain quality                                |


## Back-end Implementation
### API Specification

| **No** | **HTTP Method** | **URL**                          | **Purpose**                                             | **Request Body**                                                                                              | **Successful Response Code** | **Authentication and Authorization** |
|--------|------------------|----------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------|
| 1      | POST             | /users                          | Create New User Account                                 | `{"firstName":"string", "lastName":"string", "email":"string", "password":"string", "userType":"string"}`     | 201                            | All users                              |
| 2      | POST             | /users/login                    | Allow users to log in                                   | `{"email":"string", "password":"string"}`                                                                    | 200                            | All users                              |
| 3      | POST             | /users/logout                   | Allow users to log out (end active session)             | None                                                                                                         | 200                            | User Auth                              |
| 4      | GET              | /users/me                       | Get current user's details                              | None                                                                                                         | 200                            | User Auth, Admin Auth                  |
| 5      | PUT              | /users/me                       | Update user account                                     | `{"firstName":"string", "lastName":"string", "email":"string", "password":"string"}`                         | 200                            | User Auth, Admin Auth                  |
| 6      | DELETE           | /users/me                       | Delete user account and all associated speaker profiles | None                                                                                                         | 204                            | User Auth, Admin Auth                  |
| 7      | GET              | /portfolios                     | List all speaker portfolios                             | None                                                                                                         | 200                            | All users                              |
| 8      | POST             | /portfolios                     | Create new profile                                      | `{"profileName":"string", "profilePhoto":"string", "location":"string", "specializations":["string"], "experienceLevel":"string", "bio":"string", "contactPreferences":{}}` | 201                            | User Auth, Admin Auth                  |
| 9      | GET              | /portfolios/:id                 | Get single profile details                              | None                                                                                                         | 200                            | All users                              |
| 10     | PUT              | /portfolios/:id                 | Update existing profile                                 | `{"profileName":"string", "profilePhoto":"string", "location":"string", "specializations":["string"], "experienceLevel":"string", "bio":"string", "contactPreferences":{}}` | 200                            | User Auth, Admin Auth                  |
| 11     | DELETE           | /portfolios/:id                 | Delete specific profile                                 | None                                                                                                         | 204                            | User Auth, Admin Auth                  |
| 12     | GET              | /portfolios/search/name or location | Search profiles with filters                           | Query param: `Name`, `Location`, `Specialisation`                                                           | 200                            | All users                              |
| 13     | GET              | /portfolios/:id/likes           | Retrieve the number of likes on a profile              | None                                                                                                         | 200                            | All users                              |

### Database Schema
![Database Schema V2](./README_images/databaseSchema-v2.png)

## Front-end Implementation

### Wireframes

See V1 (completed Saturday 11 January 2025) of Wireframes [here](https://excalidraw.com/#room=c17972f48f4322229496,9WDLADVu3hiEHfNN1ABdPA)

#### Design Inspiration
![Design Inspiration](./README_images/design-inspiration.png)

#### Wireframes - Version 1
![Wireframe: homepage](./README_images/wireframes.png)

#### Wireframe - HOME
![Wireframe - HOME](./README_images/1-wireframe-home.png)

#### Wireframe - LOGIN
![Wireframe - LOGIN](./README_images/2-wireframe-login.png)

#### Wireframe - SIGNIN
![Wireframe - SIGNIN](./README_images/3-wireframe-signin.png)

#### Wireframe - SHOWING RESULTS
![Wireframe - SHOWING RESULTS](./README_images/4-wireframe-showingResults.png)

#### Wireframe - PROFILE
![Wireframe - PROFILE](./README_images/5-wireframe-profile.png)

#### Wireframe - CREATE PROFILE
![Wireframe - CREATE PROFILE](./README_images/6-wireframe-createProfile.png)

#### Wireframe - ERROR PAGE
![Wireframe - ERROR PAGE](./README_images/7-wireframe-errorPage.png)

#### Wireframe - PAGE NO RESULT
![Wireframe - PAGE NO RESULT](./README_images/8-wireframe-pageNoResult.png)

## Style Guide

### Option 1: AESOP Style

![AESOP Style Guide](./README_images/style-aesop.png)

### Typography
#### Headings
- Font: Playfair Display
- Source: [Google Fonts - Playfair Display](https://fonts.google.com/specimen/Playfair+Display)
- Usage: Main headings, Navigation text, Important text content

#### Body Text
- Font: Inter
- Source: [Google Fonts - Inter](https://fonts.google.com/specimen/Inter)
- Usage: Body text and general content

### Color Palette
#### Primary Colors
- Black (`#000000`)
  - Usage: Main headings, Navigation text, Important text content, Primary buttons, Footer text

#### Secondary Colors
- White (`#FFFFFF`)
  - Usage: Page background, Input field backgrounds, Modal backgrounds, Card backgrounds, Profile cards

#### Accent Colors
1. Orange (`#FF6600`)
   - Usage: Call-to-action buttons, Selected states, Important indicators, Links hover states, Highlighted text
2. Light Gray (`#F5F5F5`)
   - Usage: Secondary backgrounds, Input field borders, Less prominent elements, Disabled states, Dividers

### Interactive Elements
- Primary Button (Black background, White text)
- Secondary Button (White background, Black border)
- States:
  - Inactive State (Light gray)
  - Active State (Orange background)
  - Disabled State (Light gray)

## Option 2: Sunroom Style

![Sunroom Style Guide](./README_images/style-sunroom.png)

### Typography
#### Headings
- Font: Helvetica Neue or Archivo
- Sources: 
  - [Adobe Fonts - Helvetica Neue](https://fonts.adobe.com/fonts/helvetica-neue)
  - [Google Fonts - Archivo](https://fonts.google.com/specimen/Archivo)
- Usage: All headings and titles

#### Body Text
- Font: Roboto
- Source: [Google Fonts - Roboto](https://fonts.google.com/specimen/Roboto?query=ROBOTO)
- Usage: Body text and general content

### Color Palette
#### Primary Colors
- Black (`#000000`)
  - Usage: Headings, Buttons, Primary text, Navigation links, Footer text

#### Secondary Colors
- White (`#FFFFFF`)
  - Usage: Background, Profile cards, Card backgrounds, Input fields, Error pages

#### Accent Colors
1. Burnt Orange (`#D35400`)
   - Usage: Buttons, Links, Interactive elements, Active elements, Highlighted fields
2. Soft Gray (`#E0E0E0`)
   - Usage: Borders for input fields, Secondary backgrounds, Disabled states, Background for less prominent elements

### Interactive Elements
- Primary Button (Black background, White text)
- Secondary Button (White background, Black border)
- States:
  - Inactive State (Light gray)
  - Active State (Orange background)
  - Disabled State (Light gray)

## Option 3: Hinge Style

![Hinge Style Guide](./README_images/style-hinge.png)

### Typography
#### Headings
- Font: Cormorant Garamond
- Source: [Google Fonts - Cormorant Garamond](https://fonts.google.com/specimen/Cormorant+Garamond)
- Usage: All headings and titles

#### Body Text
- Font: Open Sans
- Source: [Google Fonts - Open Sans](https://fonts.google.com/specimen/Open+Sans?query=OPEN+SANS)
- Usage: Body text and general content

### Color Palette
#### Primary Colors
- Soft Black (`#1A1A1A`)
  - Usage: Headings, Buttons, Primary content, Footer text, Navigation links

#### Secondary Colors
- White (`#FFFFFF`)
  - Usage: Background, Profile cards, Card backgrounds, Modal backgrounds, Input fields

#### Accent Colors
1. Orange (`#FF6600`)
   - Usage: Buttons, Links, Call to actions, Active elements, Highlighted fields
2. Light Gray (`#E0E0E0`) or Soft Orange (`#FFC299`)
   - Usage: Borders for input fields, Dividers, Background for less prominent elements, Disabled states

### Interactive Elements
- Primary Button (Soft Black background, White text)
- Secondary Button (White background, Soft Black border)
- Text Styles:
  - Heading Text
  - Body Text
  - Link Text (Orange)
- States:
  - Inactive State (Light gray)
  - Active State (Orange background)
  - Disabled State (Light gray)

## Icons
The following icon sets are available for use across all style options:
- [FontAwesome](https://fontawesome.com)
- [Feather Icons](https://feathericons.com)
- [Material Icons](https://fonts.google.com/icons)

### Common Icons Used
- Search Icon
- User Profile Icon
- Dropdown Icon
- Pagination Icons
- Error Icon
- Edit Icon
- Save Icon