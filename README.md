# Django Signals - Same Thread Execution  

## Overview  
This project demonstrates how *Django signals* execute within the *same thread* and how they behave during a transaction.  

## Steps to Run  

1. *Clone the Repository*  
   ```sh
   git clone <your-repo-url>
   cd <your-project-folder>

2. Setup Virtual Environment & Install Dependencies

python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
pip install -r requirements.txt


3. Run Migrations & Start Server

python manage.py migrate  
python manage.py runserver


4. Test in Django Shell

python manage.py shell

Create a test instance

from myapp.models import MyModel  
instance = MyModel.objects.create(name="Test Object")
