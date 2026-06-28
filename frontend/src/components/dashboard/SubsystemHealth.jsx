import "./SubsystemHealth.css";

const systems = [
    "Power",
    "Battery",
    "Thermal",
    "Communication",
    "ADCS",
    "OBC",
];

function SubsystemHealth() {
    return (
        <section className="subsystem-health">

            <div className="subsystem-header">
                <h3>Subsystem Health</h3>
            </div>

            <div className="subsystem-grid">

                {systems.map((system) => (
                    <div className="system-card" key={system}>

                        <div className="circle">
                            --
                        </div>

                        <span>{system}</span>

                    </div>
                ))}

            </div>

        </section>
    );
}

export default SubsystemHealth;