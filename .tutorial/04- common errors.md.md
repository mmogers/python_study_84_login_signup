# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Key Error

👉 What's the problem here?


```python
@app.route("/changePass", methods=["POST"])

def change():
  form = request.form
  
  db["test"] ["password"]= request.form["newPassword"]
  return f"""Password changed to {request.form['newPassword']}"""
```

<details> <summary> 👀 Answer </summary>

I was trying to access the database key `test`, which doesn't exist.

This is where `try... except` comes in really handy, because the error messages thrown by an error like this are really horrible.

```python
@app.route("/changePass", methods=["POST"])

def change():
  form = request.form
  
  db[request.form["username"]] ["password"]= request.form["newPassword"]
  return f"""Password changed to {request.form['newPassword']}"""
```

</details>

## Informal

👉 What's the problem here?


```html

    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email"> </p>
    <p>Website: <input type="url" name="website"> </p>
    <p>Age: <input type="number" name="age"> </p>
    <input type="hidden" name="userID" value="232"> </p>

    <p>
      Fave Baldy: 
      <select name="baldies">
        <option>David</option>
        <option>Jean Luc Picard</option>
        <option>Yul Brynner</option>
      </select>
    </p>

    <button type="submit">Save Data</button>
  
```

<details> <summary> 👀 Answer </summary>

The form was not inside `<form>` tags.  This won't look any different, but saving data just won't work. 

```html
<form>
    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email"> </p>
    <p>Website: <input type="url" name="website"> </p>
    <p>Age: <input type="number" name="age"> </p>
    <input type="hidden" name="userID" value="232"> </p>

    <p>
      Fave Baldy: 
      <select name="baldies">
        <option>David</option>
        <option>Jean Luc Picard</option>
        <option>Yul Brynner</option>
      </select>
    </p>

    <button type="submit">Save Data</button>
  </form>
```
</details>