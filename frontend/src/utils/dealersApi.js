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
      method: 'GET',
      headers: {
        ...this._headers,
      },
    })
    .then(this._checkResponse)
  }

  getItemToMatch(id) {
    return fetch(`${this._baseUrl}/dialer_prices/${id}/`, {
      method: 'GET',
      headers: {
        ...this._headers,
      },
    })
    .then(this._checkResponse)
  }

  getDataToMatch(id) {
    return fetch(`${this._baseUrl}/dialer_prices/${id}/get_data_for_marking/`, {
      method: 'GET',
      headers: {
        ...this._headers,
      },
    })
    .then(this._checkResponse)
  }
  
  setMatch(id, pr_id) {
    return fetch(`${this._baseUrl}/dialer_prices/${id}/set_link_with_product/${pr_id}/`, {
      method: 'POST',
      headers: {
        ...this._headers,
      },
    })
    .then(this._checkResponse)
  }

  deleteMatch(id) {
    return fetch(`${this._baseUrl}/dialer_prices/${id}/set_link_with_product/0/`, {
      method: 'POST',
      headers: {
        ...this._headers,
      },
    })
    .then(this._checkResponse)
  }
}

const dealersApi = new DealersApi(
  `http://127.0.0.1:8000/api/v1`,
  {
    'Content-Type': 'application/json'
  }
)

export {dealersApi};