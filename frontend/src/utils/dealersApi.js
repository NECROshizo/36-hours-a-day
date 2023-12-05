class DealersApi {
  constructor(baseUrl, headers) {
    this._baseUrl = baseUrl;
    this._headers = headers;
  }

  _checkResponse(res) {
    if (res.ok) {
      return res.json();
    }
    return Promise.reject(`Ошибка: ${res.status}`);
  }

  getDealerProducts() {
    return fetch(`${this._baseUrl}/dialer_prices/`, {
      headers: {
        ...this._headers,
      },
    })
    .then(this._checkResponse)
  }
}


const dealersApi = new DealersApi(
  `https://editor.swagger.io/api/v1`,
  {
    'Content-Type': 'application/json'
  }
)

export {dealersApi};