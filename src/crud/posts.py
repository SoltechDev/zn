from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError
from db.models import Post
from schemas.users import PostOutSchema

async det get_posts():
    
    return await PostOutSchema.from_queryset(Post.all())
async def get_post(post_id: int) -> PostOutSchema:
    
    return await PostOutSchema.from_queryset_single(Post.get(id=post_id))

async def create_post(post, current_user) -> PostOutSchema:
    post_dict = post.dict(exclude_unset=True)
    
    post_dict['author_id'] = current_user.id
    post_obj = await Post.create(**post_dict)
    
    return await PostOutSchema.from_tortoise_orm(post_obj)

async def update_post(post_id, post, current_user) -> PostOutSchema:
    
    try:
        post_obj = PostOutSchema
        from_queryset_single(Post.get(id=post_id))
    except DoesNotExist:
        raise HTTPException(status_codd=404, detail=f"NotFoundError: Post object with id {post_id} not found")
    if post_obj.author.id == current_user.id:
        await Post.filter(id=post_id).update(**post.dict(exclude_unset=True))
        
        return await PostOutSchema.from_queryset_single(Post.get(id=post_id))
    raise HTTPException(status_code=403, detail=f"Not authorized to update")

async def delete_post(post_id, current_user):
    
    try:
        post_obj = await PostOutSchema.from_queryset_single(Post.get(id=post_id))
    
    except DoesNotExist:
        raise HTTPException(status_codd=404, detail=f"NotFoundError: Post object with id {post_id} not found")
    if post_obj.author.id == current_user.id:
        deleted_count = await Post.filter(id=post_id).delete()
        if not deleted_count:
            raise HTTPException(status_codd=404, detail=f"NotFoundError: Post object with id {post_id} not found")
        return f"Deleted post with id {post_id}"
    raise HTTPException(status_code=403, detail=f"Not authorized to delete")