import './App.css';
import { useEffect, useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from '../Header/Header';
import Main from '../Main/Main';
import Item from '../Item/Item';
import {dealersApi} from '../../utils/dealersApi';
import {ITEMS} from '../../constants/constants';


function App() {

  const matchedItems = [
    {
      id: 1,
      dealerKey: 2,
      name: 'itemProsept2'
    },
    {
      id: 2,
      dealerKey: 4,
      name: 'itemProsept1'
    },
    {
      id: 3,
      dealerKey: 6,
      name: 'itemProsept6'
    },
    {
      id: 4,
      dealerKey: 8,
      name: 'itemProsept5'
    }
  ]
  const [items, setItems] = useState([]);
  const [itemToMatch, setItemToMatch] = useState({});

  useEffect(() => {
    const storedItem = localStorage.getItem('itemToMatch');
    if (storedItem) {
      setItems(JSON.parse(storedItem));
    }
  }, []);

  function onItemClick(item) {
    setItemToMatch(item);
    localStorage.setItem('itemToMatch', JSON.stringify(item));
  }

  function onSearchMatch(matchedItems, item) {
    const prosept = (matchedItems.filter((matchedItem) => matchedItem.dealerKey === item.id)[0]);
    if (prosept) {
      return prosept.name
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
            matchedItems={matchedItems}
            onItemClick={onItemClick}
            onSearchMatch={onSearchMatch}
          />}
        />

        <Route path={`/${itemToMatch.id}`}
          element={<Item
            itemToMatch={itemToMatch}
            setItemToMatch={setItemToMatch}
            matchedItems={matchedItems}
            onSearchMatch={onSearchMatch}
          />}
        />
      </Routes>
    </div>
  );
}

export default App;
