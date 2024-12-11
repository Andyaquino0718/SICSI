async function updateLight(lightId, state) {
    const response = await fetch(`/update-light/${lightId}/${state}`, { method: 'POST' });
    const result = await response.json();
    if (result.success) {
        console.alert(result.message);
    } else {
        console.alert(result.message);
    }
}

function startAutomaticCycle() {
    const lights = ['light1', 'light2', 'light3'];
    let currentStates = {
        light1: 'red',
        light2: 'green',
        light3: 'yellow',
    };

    setInterval(async () => {
        for (const light of lights) {
            let currentState = currentStates[light];
            let nextState = getNextState(currentState);
            await updateLight(light, nextState);
            currentStates[light] = nextState;
        }
    }, 1000);

    function getNextState(currentState) {
        switch (currentState) {
            case 'red':
                return Math.random() *1+1 ? 'green' : 'red';
            case 'green':
                return Math.random() *1+1 ? 'yellow' : 'green'; 
            case 'yellow':
                return Math.random() *1+1 ? 'red' : 'yellow';
            default:
                return currentState;
        }
    }
}


window.onload = startAutomaticCycle;