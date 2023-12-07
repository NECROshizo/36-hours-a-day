import './Item.css';
import {Link} from 'react-router-dom';
import { useState } from 'react';

function Item({itemToMatch, setItemToMatch, matchedItems, onSearchMatch}) {

  const [value, setValue] = useState('');

  function handleFindMatched(matchedItems, item) {
    return onSearchMatch(matchedItems, item)
  }

  function handleChange(e) {
    setValue(e.target.value);
    console.log(value);
  }

  return (
    <section className='item'>
      <div className='item__dealer-info'>
        <p className='item__prod-name'>{itemToMatch.product_name}</p>
        <p className='item__price'>{itemToMatch.price}</p>
        <p className='item__price'>Артикул: {itemToMatch.product_key}</p>
        <p className='item__price'>Дилер: {itemToMatch.dealer.name}</p>
      </div>
      <form className='item__match-search'>
        <label className='item__proposap-title'>{handleFindMatched(matchedItems, itemToMatch)}</label>
        <select className='item__match-proposal'
          value={value}
          onChange={handleChange}
          >
            <option className='item__proposal-name'>Предложение 1</option>
            <option className='item__proposal-name'>Предложение 2</option>
            <option className='item__proposal-name'>Предложение 3</option>
            <option className='item__proposal-name'>Предложение 4</option>
            <option className='item__proposal-name'>Предложение 5</option>
        </select>
        <div className='item__buttons'>
          <button className='item__button'>Да</button>
          <button className='item__button'>Нет</button>
          <Link to='/' className='item__back-link'>Отложить</Link>
        </div>
      </form>
    </section>
  )
}

export default Item;
