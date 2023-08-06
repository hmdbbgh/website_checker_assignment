====================
Mentoring Assignment
====================

**Contents:**

.. contents:: :local:

Instruction
-----------

Step 1.
~~~~~~~
**Install Virtual Environment (venv):**
    For Linux:
        
        .. code-block:: bash

            sudo apt install python3.10-venv

    For Windows:
    
        .. code-block:: bash

            pip install virtualenv

Step 2.
~~~~~~~
**Create a Virtual Environment:**

    For Linux:
        
        .. code-block:: bash

            python3.10 -m venv venv

    For Windows:
    
        .. code-block:: bash

            virtualenv venv

Step 3.
~~~~~~~
**Activate your Virtual Environment:**

    For Linux:
        
        .. code-block:: bash

            source venv/bin/activate

    For Windows:
    
        .. code-block:: bash

            venv\Scripts\activate.bat

Step 4.
~~~~~~~
**Install required packages from requirements.txt:**

.. code-block:: bash

    pip install -r requirements.txt

Step 5.
~~~~~~~
**Create settings.ini:**

    For Linux:
        
        .. code-block:: bash

            cp .env.sample .env

    For Windows:
    
        .. code-block:: bash

            copy .env.sample .env

Step 6.
~~~~~~~
**Docker compose up:**

.. code-block:: bash

    docker-compose -f docker-compose.yml up -d --build

Step 7.
~~~~~~~
**Migrate the basic migrations:**

.. code-block:: bash

    python main.py
