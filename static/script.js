document.addEventListener('DOMContentLoaded', function() {
    const constructorAModels = {
        'Cisco': ['C887', 'C888EA'],
        'Juniper': ['SRX300', 'SRX320']
    };

    const modelBMapping = {
        'C887': { 'Cisco': 'C1117' },
        'C888EA': { 'Juniper': 'SRX320' },
        'SRX300': { 'Cisco': 'C1117' },
        'SRX320': { 'Cisco': 'C887' }
    };

    const constructeurASelect = document.getElementById('constructeurA');
    const modeleASelect = document.getElementById('modeleA');
    const constructeurBSelect = document.getElementById('constructeurB');
    const modeleBSelect = document.getElementById('modeleB');

    function updateModels() {
        const selectedConstructorA = constructeurASelect.value;
        const models = constructorAModels[selectedConstructorA] || [];
        
        // Clear and populate modeleA select
        modeleASelect.innerHTML = '<option value="">Select Model A</option>';
        models.forEach(model => {
            const option = document.createElement('option');
            option.value = model;
            option.textContent = model;
            modeleASelect.appendChild(option);
        });

        // Clear constructeurB and modeleB select
        constructeurBSelect.innerHTML = '<option value="">Select Constructor B</option>';
        modeleBSelect.innerHTML = '<option value="">Select Model B</option>';
    }

    function updateAvailableConstructors() {
        const selectedModelA = modeleASelect.value;
        const availableConstructors = Object.keys(modelBMapping[selectedModelA] || {});
        
        // Clear and populate constructeurB select
        constructeurBSelect.innerHTML = '<option value="">Select Constructor B</option>';
        availableConstructors.forEach(constructor => {
            const option = document.createElement('option');
            option.value = constructor;
            option.textContent = constructor;
            constructeurBSelect.appendChild(option);
        });

        // Clear modeleB select
        modeleBSelect.innerHTML = '<option value="">Select Model B</option>';
    }

    function updateModelB() {
        const selectedModelA = modeleASelect.value;
        const selectedConstructorB = constructeurBSelect.value;
        const modelB = modelBMapping[selectedModelA]?.[selectedConstructorB];

        // Clear and populate modeleB select
        modeleBSelect.innerHTML = '<option value="">Select Model B</option>';
        if (modelB) {
            const option = document.createElement('option');
            option.value = modelB;
            option.textContent = modelB;
            modeleBSelect.appendChild(option);
        }
    }

    constructeurASelect.addEventListener('change', updateModels);
    modeleASelect.addEventListener('change', updateAvailableConstructors);
    constructeurBSelect.addEventListener('change', updateModelB);
});
