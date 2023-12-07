import './App.css';
import { useEffect, useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from '../Header/Header';
import Main from '../Main/Main';
import Item from '../Item/Item';
import {dealersApi} from '../../utils/dealersApi';


function App() {

  const [items, setItems] = useState([]);
  const [itemToMatch, setItemToMatch] = useState({});
  const [proposals, setProposals] = useState([]);

  useEffect(() => {
    const storedItem = localStorage.getItem('itemToMatch');
    if (storedItem) {
      setItemToMatch(JSON.parse(storedItem));
    }
  }, []);

  function onItemClick(item) {
    setItemToMatch(item);
    localStorage.setItem('itemToMatch', JSON.stringify(item));
    dealersApi.getDataToMatch(itemToMatch.product_key)
      .then((data) => {
        setProposals(data);
      })

  }

  function onSearchMatch(item) {
    const prosept = item.product_cust;
    if (prosept) {
      return prosept
    } else return ''
  }

  useEffect(() => {
    const storedItems = localStorage.getItem('items');
    if (storedItems) {
      setItems(JSON.parse(storedItems));
    } else {
      dealersApi.getDealerProducts()
      .then((data) => {
        setItems(data.results);
        localStorage.setItem('items', JSON.stringify(data.results))
      })
      .catch((err) => {
        console.log(`Ошибка: ${err}`)
      })
    }
  }, [])
  

  return (
    <div className='page'>
      <Header
      />
      <Routes>
        <Route path='/'
          element={<Main
            items={items}
            itemToMatch={itemToMatch}
            onItemClick={onItemClick}
            onSearchMatch={onSearchMatch}
          />}
        />

        <Route path={`/${itemToMatch.id}`}
          element={<Item
            itemToMatch={itemToMatch}
            proposals={proposals}
            setItemToMatch={setItemToMatch}
            onSearchMatch={onSearchMatch}
          />}
        />
      </Routes>
    </div>
  );
}

export default App;
