$(document).ready(function() {
  var suggestions = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    remote: {
      url: 'http://localhost:5000/suggestion/%QUERY',
      dataType: 'jsonp',
      wildcard: '%QUERY'
    }
  });

  $('#suggestion .typeahead').typeahead(null, {
    name: 'suggestions',
    display: 'value',
    limit: 5,
    source: suggestions
  });
});
