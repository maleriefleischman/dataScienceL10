#get list of available cities, make it a set to automatically remove dupes
cities = set(data_back['city'].to_list())

#format the options for dropdown
options = ''
for c in cities:
    options += f'<option value="{c}">{c}</option>'

#import flast and request
from flask import Flask, request

#create app
app = Flask("5th app")

#create route
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        # Display a form for the user to input their name
        return f'''<form method="POST">
                    <label for="cities">Select a city:</label>
                    <select name="cities" id="cities">
                    {options}
                    </select>
                    <button type="submit">Submit</button>
                  </form>'''
    else:
        # Process the submitted form data
        try:
            print(request.form.get('cities'))
            #filter by selected city
            result = data_back[data_back['city'] == request.form.get('cities')]
            #return result as json objects
            return result.to_json(orient='records')
        except KeyError:
            # Handle the case where the 'city' key is not present in the form data
            return "Please select a valid city."

#run app
app.run(host='localhost', port=5008)