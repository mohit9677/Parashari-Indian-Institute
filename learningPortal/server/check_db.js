import mongoose from 'mongoose';

mongoose.connect('mongodb://127.0.0.1:27017/parashari_dev').then(async () => {
    try {
        const db = mongoose.connection.db;
        const collections = await db.listCollections().toArray();
        console.log("Collections:", collections.map(c => c.name));

        const coursesCount = await db.collection('courses').countDocuments();
        console.log("Courses count:", coursesCount);

        // Also check if there's any other database it might be using?
        const dbs = await db.admin().listDatabases();
        console.log("Databases:", dbs.databases.map(d => d.name));

    } catch (err) {
        console.error(err);
    } finally {
        process.exit(0);
    }
});
