import styles from './styles';

function Search () {
    return (
        <div style={styles.divStyle}>
            <h1 style={styles.headerStyle}>House Price Estimator</h1>
            <p style={styles.subHeaderStyle}>Put in your address to find out how much your house is worth. </p>
        
        
            <input 
                placeholder="Enter address..." 
                style={styles.inputStyle} 
                type="text" />

            <button 
                style={styles.searchButton} 
                type="submit">Search</button>
        </div>
    )
}

export default Search;