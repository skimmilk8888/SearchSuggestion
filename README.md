## Dependencies

You need to install flask, flask_restful, pytrie for python

## Start backend

First "cd" to folder "backend", then type:
```
python server.py
```
This will start a REST server locally at port 5000

## Start frontend

First "cd" to folder "frontend", then simply double click index.html to open it in a browser, start typing country names in the search box, we will give you suggestions automatically.

## Test

To run unittest, "cd" to folder "backend" and simply type:

```
python unittest_suggester.py
```

## Notes

For the backend side, we use a prefix tree to support fast lookup over data. If the data grows bigger (like millions of items), we can use some search library like Solr or ElasticSearch to build indexes for those prefixes to support efficient lookup.

For the frontend side, we use typeahead to support Ajax call to backend service and update suggestion box automatically. It used to be part of bootstrap but is now kind of a standalone library but still relies on jQuery. You can customize number of results to return, number of parallel requests, etc.