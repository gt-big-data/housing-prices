import { Routes, Route } from 'react-router-dom';
import Search from './components/Search';
import Display from './components/Display';

function App() {
  return (
    <div className="App">
    <Routes>
      <Route path='/' element={ <Search /> }></Route>
      <Route path='/result' element={ <Display /> }></Route>
    </Routes>
    </div>
  );
}

export default App;
