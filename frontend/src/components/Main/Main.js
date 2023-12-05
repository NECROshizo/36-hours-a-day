import { useEffect, useState } from 'react';
import './Main.css';

import Filter from '../Filter/Filter';
import CardList from '../CardList/CardList';

function Main({items, matchedItems, onItemClick, onSearchMatch, itemToMatch}) {

 const [statusFilter, setStatusFilter] = useState('all');
 const [filteredItems, setFilteredItems] = useState(items);


  function onFilterChange(e) {
    console.log(filteredItems);

    return setStatusFilter(e.target.value);
  }

  function checkIsMatched(matchedItems, item) {
    if (matchedItems.find((matchedItem) => matchedItem.dealerKey === item.id)) {
      return true;
    } else 
    return false;
  }

  return (
    <section className='main'>
      <Filter 
        onFilterChange={onFilterChange}
      />
      <CardList 
        items={items}
        filteredItems={filteredItems}
        matchedItems={matchedItems}
        onItemClick={onItemClick}
        onSearchMatch={onSearchMatch}
        statusFilter={statusFilter}
        checkIsMatched={checkIsMatched}
        itemToMatch={itemToMatch}
      />
    </section>
  );
}

export default Main;