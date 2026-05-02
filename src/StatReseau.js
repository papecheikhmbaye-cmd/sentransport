import "./StatReseau.css";

function StatReseau({ lignes }) {
  if (lignes.length === 0) {
    return <div>Aucune donnée</div>;
  }

  const nombreTotalLigne = lignes.length;

  let nombreTotalArrets = 0;
  for (let i = 0; i < lignes.length; i++) {
    nombreTotalArrets += lignes[i].arrets;
  }

  let ligneMax = lignes[0];
  for (let i = 1; i < lignes.length; i++) {
    if (lignes[i].arrets > ligneMax.arrets) {
      ligneMax = lignes[i];
    }
  }

  return (
    <div className="StatReseau">
      <span>Nombre total de lignes : {nombreTotalLigne}</span>
      <span>Nombre total d'arrêts : {nombreTotalArrets}</span>
      <span>
        Ligne avec le plus d'arrêts : Ligne {ligneMax.numero} ({ligneMax.arrets}{" "}
        arrêts)
      </span>
    </div>
  );
}

export default StatReseau;
