(function() {
    let cy = cytoscape({
    container: document.getElementById('cy'),
    layout: {
        name: 'random'
    },
    elements: [
        {
            group: 'nodes',
            data: {id: 'n1'}
        },
        {
            group: 'nodes',
            data: {id: 'n2'}
        },
        {
            group: 'nodes',
            data: {id: 'n3'}
        },
        {
            group: 'nodes',
            data: {id: 'n4'}
        },
        {
            group: 'nodes',
            data: {id: 'n5'}
        },
        {
            data: {
                id: 'e1',
                source: 'n1',
                target: 'n4'
                }
        },
        {
            data: {
                id: 'e2',
                source: 'n1',
                target: 'n2'
                }
        },
        {
            data: {
                id: 'e3',
                source: 'n2',
                target: 'n3'
                }
        },
        {
            data: {
                id: 'e4',
                source: 'n3',
                target: 'n4'
                }
        },
        {
            data: {
                id: 'e5',
                source: 'n2',
                target: 'n5'
                }
        }]
    });
    var dfs = cy.elements().aStar({
        root: '#n1',
        goal: '#n5',
        directed: true
    })
    dfs.path.select()
    console.log(dfs.distance)
})();