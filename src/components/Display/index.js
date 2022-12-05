import styles from './styles';
import { Map } from 'pigeon-maps';
import interior1 from '../../files/interior1.jpg'
import interior2 from '../../files/interior2.jpeg'

function Display() {
    return (
        <div style={styles.container}>
            <div style={styles.metaStyle}>
                <div style={styles.infoStyle}>
                    <h1 style={styles.headerStyle}> Home Value: $999,999 </h1>
                    <p style={styles.subHeaderStyle}>3 beds | 2 baths | 1200 sq ft </p>
                    <p style={styles.subHeaderStyle}>123 Main Street, Atlanta, GA</p>
                </div>
                <div style={styles.houseStyle}>
                    <img style={styles.imageStyle} src={interior1} alt="interior 1" />
                    <img style={styles.imageStyle} src={interior2} alt="interior 1" />
                </div>
                <div style={styles.mapStyle}>
                    <Map
                        defaultCenter={[33.75, -84.39]}
                        defaultZoom={10}
                    >
                    </Map>
                </div>
            </div>


        </div>
    ) }

export default Display;
