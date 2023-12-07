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

  useEffect(() => {
    const storedProposals = localStorage.getItem('proposals');
    if (storedProposals) {
      setProposals(JSON.parse(storedProposals));
    }
  }, []);

  function handleGetProposals(itemToMatch) {
    dealersApi.getDataToMatch(itemToMatch.product_key)
      .then((data) => {
        setProposals(data);
        localStorage.setItem('proposals', JSON.stringify(data))
      })
      .catch((err) => {
        console.log(`Ошибка: ${err}`)
      })
  }

  function onItemClick(item) {
    setItemToMatch(item);
    localStorage.setItem('itemToMatch', JSON.stringify(item));
    handleGetProposals(item);
    console.log(item);
  }

  useEffect(() => {
    dealersApi.getDealerProducts()
      .then((data) => {
        setItems(data.results);
        localStorage.setItem('items', JSON.stringify(data.results))
      })
      .catch((err) => {
        console.log(`Ошибка: ${err}`)
      })
  }, [])

  function onSearchMatch(item) {
    if (item.product_cust.name) {
      return item.product_cust.name;
    } else return ''
  }  

  return (
    <div className='page'>
      <Header/>
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
            setItemToMatch={setItemToMatch}
            onSearchMatch={onSearchMatch}
            proposals={proposals}
            setProposals={setProposals}
          />}
        />
      </Routes>
    </div>
  );
}

export default App;
