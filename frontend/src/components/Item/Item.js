import './Item.css';
import {Link} from 'react-router-dom';
import { useEffect, useState } from 'react';
import {dealersApi} from '../../utils/dealersApi';


function Item({itemToMatch, setItemToMatch, proposals}) {

  const [itemValue, setItemValue] = useState(0);
  const [isMatched, setIsMatched] = useState(itemToMatch.is_defined);

  useEffect(() => {
    setIsMatched(itemToMatch.is_defined);
  }, [])

  function handleChange(e) {
    setItemValue(e.target.value);
  }
/*
  function showOwnProduct(id) {
    dealersApi.getOwnProduct(id)
      .then((data) => {
        setIsMatched(true);
      })
      .then(() => console.log(matchedProduct))
      .catch((err) => {
        console.log(`Ошибка: ${err}`)
      })
    }
*/
  function handleSetMatch(e) {
    e.preventDefault();
    dealersApi.setMatch(itemToMatch.product_key, itemValue)
      .then(() => {
      localStorage.setItem('matchedId', itemValue);
      dealersApi.getItemToMatch(itemToMatch.product_key)
        .then((data) => {
          setItemToMatch(data);
          setIsMatched(true);
        })
        .catch((err) => {
          console.log(`Ошибка: ${err}`)
        })
      })
      .catch((err) => {
        console.log(`Ошибка: ${err}`)
      })
  }

  function handleResetMatch(e) {
    e.preventDefault();
    const del = 0;
    dealersApi.deleteMatch(itemToMatch.product_key, del)
    .then(() => {
      setIsMatched(false);
    })
    .catch((err) => {
      setIsMatched(false);
      console.log(`Ошибка: ${err}`);
    })
  }

  return (
    <section className='item'>
      <div className='item__dealer-info'>
        <p className='item__prod-name'>{itemToMatch.product_name}</p>
        <p className='item__info'>{itemToMatch.price}</p>
        <p className='item__info'>Артикул: {itemToMatch.product_key}</p>
      </div>
      <form className='item__match-search' id='match-search'>
        <label className='item__proposap-title'>{isMatched ? `${itemToMatch.product_cust.name}` : ''}</label>
        <select className='item__match-proposal'
          onChange={handleChange}
          >
            <option className='item__proposal-name'>Выберете товар</option>
            {
              proposals.map((item) => (
                <option className='item__proposal-name'
                  id={item.id}
                  value={item.id}
                  key={item.id}>
                    {item.name}
                </option>
              ))
            }
        </select>
        <div className='item__buttons'>
          <button className='item__button' type='submit' onClick={handleSetMatch} form='match-search'>Да</button>
          <button className='item__button' type='submit' onClick={handleResetMatch}>Нет</button>
          <Link to='/' className='item__back-link'>Отложить</Link>
        </div>
      </form>
    </section>
  )
}

export default Item;
