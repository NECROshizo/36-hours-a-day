import './Item.css';
import {Link} from 'react-router-dom';
import { useState } from 'react';
import {dealersApi} from '../../utils/dealersApi';


function Item({itemToMatch, proposals}) {
/*
  const proposals = [
    {
      pr_id: 1,
      name: 'Предложение 1'
    },
    {
      pr_id: 2,
      name: 'Предложение 2'
    },
    {      
      pr_id: 3,
      name: 'Предложение 3'
    },
    {
      pr_id: 4,
      name: 'Предложение 4'
    },
    {
      pr_id: 5,
      name: 'Предложение 5'
    },
  ]
*/
  const [value, setValue] = useState(proposals[0].pr_id);
  const [isMatched, setIsMatched] = useState(itemToMatch.is_defined)

  function handleChange(e) {
    setValue(e.target.value);
    console.log(value);
  }

  function handleSetMatch(e) {
    e.preventDefault();
    console.log(value);
    dealersApi.setMatch(itemToMatch.product_key, value)
      .then(() => {
      setIsMatched(true);  
      })
      .catch((err) => {
        console.log(`Ошибка: ${err}`)
      })
  }

  function handleResetMatch(e) {
    e.preventDefault();
    dealersApi.setMatch(itemToMatch.product_key, value)
    .then(() => {
      setIsMatched(false);
    })
    .catch((err) => {
      console.log(`Ошибка: ${err}`)
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
        <label className='item__proposap-title'>{isMatched ? `${itemToMatch.product_cust}` : ''}</label>
        <select className='item__match-proposal'
          onChange={handleChange}
          >
            {
              proposals.map((item) => (
                <option className='item__proposal-name'
                  value={item.pr_id}
                  key={item.pr_id}>
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
