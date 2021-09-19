const httpRequest = require('https');

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
};

const data = `{
  "GameId": 432,
  "addonIds": [],
  "featuredCount": 6,
  "popularCount": 14,
  "updatedCount": 14
}`;

const request = httpRequest.request('https://addons-ecs.forgesvc.net/api/v2/addon/featured', options, response => {
  console.log('Status', response.statusCode);
  console.log('Headers', response.headers);
  let responseData = '';

  response.on('data', dataChunk => {
    responseData += dataChunk;
  });
  response.on('end', () => {
    console.log('Response: ', responseData)
  });
});

request.on('error', error => console.log('ERROR', error));

request.write(data);
request.end();