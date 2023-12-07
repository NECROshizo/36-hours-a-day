import { useEffect, useState } from 'react';
import './Main.css';

import Filter from '../Filter/Filter';
import CardList from '../CardList/CardList';

function Main({items, matchedItems, onItemClick, onSearchMatch, itemToMatch}) {

 const [statusFilter, setStatusFilter] = useState('all');
 const [filteredItems, setFilteredItems] = useState(items);


  function onFilterChange(e) {
    return setStatusFilter(e.target.value);
  }

  function checkIsMatched(item) {
    if (item.is_defined) {
      return true;
    } else 
    return false;
  }

  function handleFilterItems(items) {
    if (statusFilter === 'yes') {
      setFilteredItems(items.filter((item) => {
        if (item.is_defined) {
          return item
        }
      }))
    } else if (statusFilter === 'no') {
      setFilteredItems(items.filter((item) => {
        if (!checkIsMatched(item)) {
          return item
        }
      }))
    } else setFilteredItems(items)
  }

  useEffect(() => {
    setFilteredItems(items)
  }, [items])

  useEffect(() => {
    handleFilterItems(items, matchedItems);
  }, [statusFilter])

  useEffect(() => {
    handleFilterItems(items, matchedItems);
  }, [])


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