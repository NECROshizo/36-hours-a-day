import './App.css';
import { useEffect, useState, useRef } from 'react';
import { Routes, Route, useLocation, useNavigate, Navigate } from 'react-router-dom';
import Header from '../Header/Header';
import Main from '../Main/Main';
import Item from '../Item/Item';
import {dealersApi} from '../../utils/dealersApi';
import {ITEMS} from '../../constants/constants';


function App() {
  const items = [
  {	
    id: 1,
    productKey: 546227,
    price: 233.00,
    //product__url: url('https://akson.ru//p/sredstvo_universalnoe_prosept_universal_spray_500ml/'),
    name: 'РЎСЂРµРґСЃС‚РІРѕ СѓРЅРёРІРµСЂСЃР°Р»СЊРЅРѕРµ Prosept Universal Spray, 500РјР',
    date: '2010.1.24'
  },
  {
    id: 2,
    productKey: 1,
    price: 100,
  //  url: norikov.notion.site,
  name: 'item1',
  date: '2010.1.24'
  },{
    id: 3,
    productKey: 1,
    price: 100,
  //  url: norikov.notion.site,
  name: 'item1',
  date: '2010.1.24'
  },{
    id: 4,
    productKey: 1,
    price: 100,
  //  url: norikov.notion.site,
  name: 'item1',
  date: '2010.1.24'
  },
  {
    id: 5,
    productKey: 1,
    price: 100,
  //  url: norikov.notion.site,
  name: 'item1',
  date: '2010.1.24'
  },
  {
    id: 6,
    productKey: 1,
    price: 100,
  //  url: norikov.notion.site,
  name: 'item1',
  date: '2010.1.24'
  },
  {
    id: 7,
    productKey: 1,
    price: 100,
  //  url: norikov.notion.site,
  name: 'item1',
  date: '2010.1.24'
  },
  {
    id: 8,
    productKey: 1,
    price: 100,
  //  url: norikov.notion.site,
  name: 'item1',
  date: '2010.1.24'
  }
] 
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
//  const [items, setItems] = useState([ITEMS]);
  const [itemToMatch, setItemToMatch] = useState({});

  useEffect(() => {
    const storedItem = localStorage.getItem('itemToMatch');
    if (storedItem) {
      setItemToMatch(JSON.parse(storedItem));
    }
  }, []);


  function onItemClick(item) {
    setItemToMatch(item);
    localStorage.setItem('itemToMatch', JSON.stringify(item));
  //  localStorage.clear();
  }

  function onSearchMatch(matchedItems, item) {
    const prosept = (matchedItems.filter((matchedItem) => matchedItem.dealerKey === item.id)[0]);
    if (prosept) {
      return prosept.name
    } else return ''
  }
/*
  useEffect(() => {
    dealersApi.getDealerProducts()
      .then((data) => {
        setItems(data);
      })
      .catch((err) => {
        console.log(`Ошибка: ${err}`)
      })
  }, [])
 */ 

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
