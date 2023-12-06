import './Item.css';
import {Link} from 'react-router-dom';

function Item({itemToMatch, setItemToMatch, matchedItems, onSearchMatch}) {

  function handleFindMatched(matchedItems, item) {
    return onSearchMatch(matchedItems, item)
  }

  return (
    <section className='item'>
      <div className='item__dealer-info'>
        <p className='item__prod-name'>{itemToMatch.name}</p>
        <p className='item__price'>{itemToMatch.price}</p>
      </div>
      <form className='item__match-search'>
        <label className='item__proposap-title'>{handleFindMatched(matchedItems, itemToMatch)}</label>
        <select className='item__match-proposal'>
          <option className='item__proposal-name'>Предложение 1</option>
          <option className='item__proposal-name'>Предложение 2</option>
          <option className='item__proposal-name'>Предложение 3</option>
          <option className='item__proposal-name'>Предложение 4</option>
          <option className='item__proposal-name'>Предложение 5</option>
        </select>
        <div className='item__buttons'>
          <button>Да</button>
          <button>Нет</button>
          <Link to='/' className='item__back-link'>Отложить</Link>
        </div>
      </form>
    </section>
  )
}

export default Item;
